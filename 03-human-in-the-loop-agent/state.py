from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List, Optional
from uuid import uuid4

class WorkflowState(Enum):
    INIT = "INIT"
    RUNNING_AUTOMATION = "RUNNING_AUTOMATION"
    WAITING_FOR_HUMAN_APPROVAL = "WAITING_FOR_HUMAN_APPROVAL"
    RESUMED_AFTER_HUMAN="RESUMED_AFTER_HUMAN"
    SUCCESS="SUCCESS"
    FAILURE="FAILURE"

class HumanDecision(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

@dataclass
class LoanApprovalState:
    """
    Shared state for the Observable & Supervised Agent.

    This state is the single source of truth and flows through
    supervisor, worker, and router nodes.
    """

    # ─────────────────────────────────────────────
    # Task identity
    # ─────────────────────────────────────────────
    
    execution_id: str = field(default_factory=lambda: str(uuid4()))
    loan_id: str = field(default_factory=lambda: str(uuid4()))
    # ─────────────────────────────────────────────
    # Execution progress
    # ─────────────────────────────────────────────
    customer_name:str=None
    loan_amount:int=None
    credit_score:float=None
    risk_level:str=None
    confidence_score:float=None
    current_state: WorkflowState =WorkflowState.INIT
    human_decision: HumanDecision = HumanDecision.PENDING
    history: List[str] = field(default_factory=list)




