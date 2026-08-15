from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from state import LoanApprovalState, WorkflowState
from nodes import (
    start_node,
    automation_node,
    supervisor_node,
    resume_after_human_node,
)
from human import human_review_node

builder = StateGraph(LoanApprovalState)

# Register nodes
builder.add_node("start_node", start_node)
builder.add_node("automation_node", automation_node)
builder.add_node("supervisor_node", supervisor_node)
builder.add_node("human_review_node", human_review_node)
builder.add_node("resume_after_human_node", resume_after_human_node)

# Linear Flow
builder.add_edge(START, "start_node")
builder.add_edge("start_node", "automation_node")
builder.add_edge("automation_node", "supervisor_node")


def route_after_supervisor(state: LoanApprovalState):

    if state.current_state == WorkflowState.SUCCESS:
        return "success"

    if state.current_state == WorkflowState.WAITING_FOR_HUMAN_APPROVAL:
        return "human"

    return "failed"


builder.add_conditional_edges(
    "supervisor_node",
    route_after_supervisor,
    {
        "success": END,
        "human": "human_review_node",
        "failed": END,
    },
)

builder.add_edge(
    "human_review_node",
    "resume_after_human_node",
)

builder.add_edge(
    "resume_after_human_node",
    "automation_node",
)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)