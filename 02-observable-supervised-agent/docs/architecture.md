# Architecture — Observable & Supervised Agent

## Section 1: System Overview

This project implements a **supervised LangGraph agent system** composed of a supervisor agent and a worker agent.

The worker agent is responsible for executing the task and performing tool calls.  
The supervisor agent is responsible for **observing task progress, evaluating output confidence, and controlling the overall execution flow**.

Supervision is required because LLM outputs can be:
- Incorrect
- Low confidence
- Partially complete
- Inconsistent across retries

By introducing a supervisor, the system gains:
- Explicit control over retries and termination
- Confidence-based decision making
- Safer and more predictable execution

Observability is treated as a first-class concern so that every important decision and transition in the agent lifecycle can be inspected and debugged.

---

## Section 2: Components and Responsibilities

### 1. Supervisor Agent
The supervisor agent acts as the **control plane** of the system.

Responsibilities:
- Read the shared state after each worker execution
- Evaluate the worker output and confidence score
- Decide one of the following actions:
  - Continue execution
  - Retry the worker
  - Terminate successfully
  - Terminate with failure
- Enforce retry limits and termination rules

The supervisor **does not call tools** and **does not generate task output**.

---

### 2. Worker Agent
The worker agent acts as the **execution plane** of the system.

Responsibilities:
- Perform the assigned task
- Call tools if required
- Produce:
  - Task output
  - Confidence score
  - Partial progress information (if applicable)

The worker **never decides when the system terminates**.

---

### 3. Router
The router is responsible for:
- Reading the supervisor’s decision
- Routing control to the next node
- Preventing invalid transitions (e.g., infinite loops)

Routing decisions are fully driven by state and supervisor output.

---

### 4. Observability Layer
The observability layer is responsible for **recording system behavior**, not influencing decisions.

Responsibilities:
- Emit structured logs for:
  - Agent steps
  - Supervisor decisions
  - Worker executions
  - Errors and retries
- Track metrics such as:
  - Execution time
  - Retry count
  - Failure frequency

The observability layer **never evaluates confidence or controls flow**.

---

### 5. Shared State
The shared state is the **single source of truth** for the entire agent lifecycle.

It is:
- Read by all components
- Updated explicitly at each step
- Used to drive routing and termination decisions

---

## Section 3: State Schema (Conceptual)

- `task`  
  The original user task to be completed.

- `current_step`  
  Indicates the current execution stage of the agent.

- `worker_output`  
  The latest output produced by the worker agent.

- `confidence_score`  
  A numeric estimate representing the worker’s confidence in its output.

- `retry_count`  
  Tracks how many times the worker has been retried.

- `max_retries`  
  Defines the maximum number of allowed retries.

- `status`  
  Represents the overall system status (e.g., running, success, failed).

- `errors`  
  Stores error information from failed executions or tool calls.

- `events`  
  A chronological record of important lifecycle events for observability.

---

## Section 4: Control Flow

1. The user submits a task.
2. The supervisor initializes the shared state.
3. The worker agent executes the task.
4. The worker updates the state with output and confidence.
5. The supervisor evaluates the updated state.
6. The router routes execution based on the supervisor’s decision:
   - Retry the worker
   - Continue execution
   - Terminate successfully
   - Terminate with failure
7. Observability signals are emitted at every step.

---

## Section 5: Termination Rules

The system terminates successfully when:
- The worker output meets confidence requirements
- The task is marked complete by the supervisor

The system terminates with failure when:
- Maximum retries are exceeded
- The supervisor detects unrecoverable errors
- Confidence remains below threshold after retries

The supervisor makes all final termination decisions.
