from dataclasses import dataclass, field
from enum import Enum
from typing import List
from uuid import uuid4


class WorkflowState(Enum):
    INIT = "INIT"
    RUNNING_AUTOMATION = "RUNNING_AUTOMATION"
    WAITING_FOR_HUMAN_APPROVAL = "WAITING_FOR_HUMAN_APPROVAL"
    RESUMED_AFTER_HUMAN = "RESUMED_AFTER_HUMAN"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class HumanDecision(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


@dataclass
class LoanApprovalState:
    retry_count: int = 0
    max_retries: int = 3

    execution_id: str = field(default_factory=lambda: str(uuid4()))
    loan_id: str = field(default_factory=lambda: str(uuid4()))

    customer_name: str | None = None
    loan_amount: int | None = None
    credit_score: float | None = None
    risk_level: str | None = None
    confidence_score: float | None = None

    current_state: WorkflowState = field(
        default_factory=lambda: WorkflowState.INIT
    )

    human_decision: HumanDecision = field(
        default_factory=lambda: HumanDecision.PENDING
    )

    history: List[str] = field(default_factory=list)