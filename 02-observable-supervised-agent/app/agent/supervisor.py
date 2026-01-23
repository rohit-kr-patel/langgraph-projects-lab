from state.schema import AgentState

SUCCESS = "SUCCESS"
RETRY = "RETRY"
FAILURE = "FAILURE"


def decide_next_action(state: AgentState) -> str:
    """
    Decide what the system should do next based on shared state.
    This function must be deterministic and side-effect free.
    """

    # 1. Terminal state checks
    if state.status == "success":
        state.status = "success"

    if state.status == "failed":
        state.status = "failed"

    # 2. Retry exhaustion
    if state.retry_count >= state.max_retries:
        return FAILURE

    # 3. Worker produced no output
    if state.worker_output is None:
        return RETRY

    # 4. Confidence check
    if state.confidence_score is not None and state.confidence_score >= 0.8:
        return SUCCESS

    # 5. Default: retry
    return RETRY
