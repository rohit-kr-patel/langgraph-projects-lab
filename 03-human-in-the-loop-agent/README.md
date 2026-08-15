# Human-in-the-Loop Loan Approval Agent using LangGraph

## Overview

This project demonstrates a **Human-in-the-Loop (HITL) workflow** using **LangGraph**. The system automates loan risk assessment based on a customer's credit score and routes uncertain cases for human review before making a final decision.

The project showcases:

* LangGraph StateGraph
* Shared workflow state
* Conditional routing
* Human-in-the-Loop using `interrupt()`
* Workflow resumption using `Command(resume=...)`
* Memory checkpointing with `MemorySaver`
* Audit history tracking

---

## Workflow Architecture

```text
START
  │
  ▼
start_node
  │
  ▼
automation_node
  │
  ▼
supervisor_node
  │
  ├──────── SUCCESS ───────► END
  │
  └──────── HUMAN REVIEW
                │
                ▼
        human_review_node
                │
          interrupt()
                │
      Workflow Paused
                │
      Human Decision
                │
                ▼
    resume_after_human_node
                │
                ▼
        automation_node
                │
                ▼
        supervisor_node
```

---

## Project Structure

```text
03-human-in-the-loop-agent/
│
├── app.py
├── graph.py
├── human.py
├── nodes.py
├── state.py
├── supervisor.py
├── failure_node.py
├── README.md
└── test_enum.py
```

---

## State Management

The workflow uses a shared state object that travels through every node.

### LoanApprovalState

```python
@dataclass
class LoanApprovalState:
    retry_count: int = 0
    max_retries: int = 3

    execution_id: str
    loan_id: str

    customer_name: str
    loan_amount: int

    credit_score: float
    risk_level: str

    confidence_score: float

    current_state: WorkflowState

    human_decision: HumanDecision

    history: List[str]
```

---

## Workflow States

```python
class WorkflowState(Enum):
    INIT = "INIT"
    RUNNING_AUTOMATION = "RUNNING_AUTOMATION"
    WAITING_FOR_HUMAN_APPROVAL = "WAITING_FOR_HUMAN_APPROVAL"
    RESUMED_AFTER_HUMAN = "RESUMED_AFTER_HUMAN"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
```

---

## Human Decisions

```python
class HumanDecision(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
```

---

## Node Responsibilities

### start_node

Initializes the workflow.

Responsibilities:

* Validates workflow starts from `INIT`
* Transitions state to `RUNNING_AUTOMATION`
* Records audit history

---

### automation_node

Performs automated risk analysis.

Rules:

| Credit Score | Risk Level | Confidence |
| ------------ | ---------- | ---------- |
| >= 750       | LOW        | 0.90       |
| 600 - 749    | MEDIUM     | 0.60       |
| < 600        | HIGH       | 0.30       |

Example:

```python
credit_score = 720

risk_level = "MEDIUM"
confidence_score = 0.60
```

---

### supervisor_node

Determines whether automation is sufficient.

Rules:

```python
if confidence_score >= 0.80:
    SUCCESS
else:
    WAITING_FOR_HUMAN_APPROVAL
```

---

### human_review_node

Implements Human-in-the-Loop.

Uses:

```python
from langgraph.types import interrupt
```

Example:

```python
decision = interrupt(
    {
        "customer_name": state.customer_name,
        "loan_amount": state.loan_amount,
        "credit_score": state.credit_score,
        "risk_level": state.risk_level,
        "confidence_score": state.confidence_score,
    }
)
```

At this point:

* Workflow pauses
* State is checkpointed
* Human reviews application
* Workflow waits for resume command

---

### resume_after_human_node

Continues execution after human review.

Responsibilities:

* Apply human updates
* Record workflow history
* Resume automation flow

---

## Human-in-the-Loop Flow

### Step 1

Start workflow:

```python
result = graph.invoke(
    initial_state,
    config=config
)
```

If confidence is low:

```python
{
    "__interrupt__": [...]
}
```

Workflow pauses.

---

### Step 2

Human reviews:

```text
Customer      : Rohit Patel
Loan Amount   : ₹500000
Credit Score  : 720
Risk Level    : MEDIUM
Confidence    : 0.60
```

Possible actions:

* Approve
* Reject
* Modify credit score

---

### Step 3

Resume workflow:

```python
from langgraph.types import Command

graph.invoke(
    Command(
        resume={
            "human_decision": "APPROVED",
            "credit_score": 790
        }
    ),
    config=config
)
```

---

## Graph Configuration

### Checkpointer

```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)
```

Purpose:

* Saves workflow state
* Enables interruption
* Allows workflow resumption

---

## Example Run

### Input

```python
LoanApprovalState(
    customer_name="Rohit Patel",
    loan_amount=500000,
    credit_score=720
)
```

### Automation Result

```text
Risk Level      : MEDIUM
Confidence Score: 0.60
```

### Supervisor Decision

```text
WAITING_FOR_HUMAN_APPROVAL
```

### Human Review

```text
Decision: APPROVED
Updated Credit Score: 790
```

### Final Result

```text
Risk Level      : LOW
Confidence Score: 0.90
Workflow State  : SUCCESS
```

---

## Learning Outcomes

This project demonstrates:

* LangGraph fundamentals
* StateGraph architecture
* Shared state management
* Conditional workflow routing
* Human-in-the-Loop workflows
* Workflow interruption and resumption
* Memory checkpointing
* Audit logging
* Multi-step business process automation

---

## Future Improvements

Potential enhancements:

* FastAPI Integration
* Web-based approval dashboard
* SQLite/PostgreSQL checkpointer
* Email approval workflow
* Slack/MS Teams approval integration
* Multi-level approval hierarchy
* Escalation and timeout handling
* Risk scoring using LLMs
* Loan fraud detection
* Workflow visualization dashboard

---

## Technologies Used

* Python 3.12
* LangGraph
* LangChain Core
* Dataclasses
* Enum
* MemorySaver Checkpointing

---

## Author

**Rohit Patel**

Human-in-the-Loop Loan Approval Workflow using LangGraph.
