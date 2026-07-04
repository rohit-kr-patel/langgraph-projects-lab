
from state import LoanApprovalState
from state import WorkflowState

def start_node(state: LoanApprovalState) -> LoanApprovalState:
    """
    Initialize the workflow and transition it from INIT
    to RUNNING_AUTOMATION.
    """

    # Guard Clause
    if state.current_state != WorkflowState.INIT:
        raise ValueError("Workflow must start from INIT state.")

    # Transition state
    state.current_state = WorkflowState.RUNNING_AUTOMATION

    # Audit log
    state.history.append(
        "State changed: INIT -> RUNNING_AUTOMATION"
    )

    return state


def automation_node(state:LoanApprovalState)-> LoanApprovalState:
    # <-- We implement this first
    if state.credit_score>=750:
        state.risk_level="LOW"
        state.confidence_score = 0.90
    elif state.credit_score<750 and state.credit_score>=600: 
        state.risk_level="MEDIUM"
        state.confidence_score = 0.60
    else:
        state.risk_level="HIGH"
        state.confidence_score = 0.30
    state.history.append(
    f"Automation completed | "
    f"Credit Score: {state.credit_score}, "
    f"Risk: {state.risk_level}, "
    f"Confidence: {state.confidence_score}"
)
    return state

def supervisor_node(state:LoanApprovalState)->LoanApprovalState:
    if state.confidence_score>=0.80:
        state.current_state=WorkflowState.SUCCESS
    else:
        state.current_state=WorkflowState.WAITING_FOR_HUMAN_APPROVAL

    state.history.append(
    f"Supervisor routed workflow to {state.current_state.value}"
)
    return state


def resume_after_human_node(state):
    pass