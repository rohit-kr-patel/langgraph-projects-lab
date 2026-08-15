from state import LoanApprovalState, WorkflowState


def failure_node(
    state: LoanApprovalState,
) -> LoanApprovalState:
    """
    Executed after all retry attempts are exhausted.
    """

    state.current_state = WorkflowState.FAILED

    print("❌ Maximum retry limit reached.")
    print("Loan moved to FAILED state.")

    # Future enhancements:
    # - Update database
    # - Send notification
    # - Publish Kafka/SQS event
    # - Write audit logs

    return state