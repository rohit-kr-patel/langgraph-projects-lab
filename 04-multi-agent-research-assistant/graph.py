from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from state import ResearchState

from nodes import (
    research_agent,
    fact_checker_agent,
    summarizer_agent,
    supervisor_agent,
)


builder = StateGraph(ResearchState)


# Nodes
builder.add_node("supervisor", supervisor_agent)
builder.add_node("research", research_agent)
builder.add_node("fact_checker", fact_checker_agent)
builder.add_node("summarizer", summarizer_agent)


# START → Supervisor
builder.add_edge(
    START,
    "supervisor",
)


# Supervisor routing
def route_next_agent(state: ResearchState):
    return state.next_agent


builder.add_conditional_edges(
    "supervisor",
    route_next_agent,
    {
        "research": "research",
        "fact_checker": "fact_checker",
        "summarizer": "summarizer",
        "end": END,
    },
)


# Agents → Supervisor
builder.add_edge(
    "research",
    "supervisor",
)

builder.add_edge(
    "fact_checker",
    "supervisor",
)

builder.add_edge(
    "summarizer",
    "supervisor",
)


# Compile
graph = builder.compile()