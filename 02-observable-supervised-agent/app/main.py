from langgraph.graph import StateGraph, END
from state.schema import AgentState
from agent.supervisor import decide_next_action
from agent.router import route
from observability.logger import log_event
from observability import metrics


def worker_node(state: AgentState) -> AgentState:
    # Dummy worker logic
    log_event("worker_started", state)
    if state.decision == "RETRY":
        state.increment_retry()
        metrics.increment_retry()

        log_event("worker_started", state)
    if state.retry_count == 0:
        state.worker_output = "partial result"
        state.confidence_score = 0.4
    else:
        state.worker_output = "final result"
        state.confidence_score = 0.9

    log_event("worker_completed", state)
    return state

def supervisor_node(state: AgentState) -> AgentState:
    decision = decide_next_action(state)
    state.decision = decision
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
    state = AgentState(task="demo task")
    final_state = app.invoke(state)
    print("Final state:", final_state)
