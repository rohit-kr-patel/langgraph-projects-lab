from langgraph.graph import StateGraph, END
from state.schema import AgentState
from agent.supervisor import decide_next_action
from agent.router import route
from observability.logger import log_event
from observability import metrics
from tools.text_analyzer import text_analyzer

def worker_node(state: AgentState) -> AgentState:
   # Retry bookkeeping (already added earlier)
    if state.decision == "RETRY":
        state.increment_retry()
        metrics.increment_retry()

    log_event("worker_started", state)

    try:
        result = text_analyzer(state.task)

        # Save factual output
        state.worker_output = result

        # Derive confidence mechanically
        wc = result["word_count"]
        if wc == 0:
            state.confidence_score = 0.0
        elif wc < 5:
            state.confidence_score = 0.4
        else:
            state.confidence_score = 0.9

    except Exception as e:
        # Tool failure path
        state.worker_output = None
        state.confidence_score = 0.0
        state.add_error(str(e))

    log_event("worker_completed", state)
    return state

def supervisor_node(state: AgentState) -> AgentState:
    decision = decide_next_action(state)
    state.decision = decision

    if decision == "SUCCESS":
        state.status = "success"

    elif decision == "FAILURE":
        state.status = "failed"

    log_event("supervisor_decision_made", state, {"decision": decision})
    return state




def start_node(state: AgentState) -> AgentState:
    metrics.increment("total_executions")
    log_event("agent_started", state)
    return state


graph = StateGraph(AgentState)

graph.add_node("start", start_node)
graph.add_node("worker", worker_node)
graph.add_node("supervisor", supervisor_node)

graph.set_entry_point("start")

graph.add_edge("start", "worker")
graph.add_edge("worker", "supervisor")

graph.add_conditional_edges(
    "supervisor",
    route,
    {
        "worker": "worker",
        "end_success": END,
        "end_failure": END,
    },
)

app = graph.compile()


if __name__ == "__main__":
    state = AgentState(task=123)
    final_state = app.invoke(state)
    print("Final state:", final_state)
