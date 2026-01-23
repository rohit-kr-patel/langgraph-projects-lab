from agent.supervisor import SUCCESS, RETRY, FAILURE
from state.schema import AgentState
def route(state: AgentState) -> str:
    if state.decision == "SUCCESS":
        return "end_success"

    if state.decision == "FAILURE":
        return "end_failure"

    return "worker"