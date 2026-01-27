# Project 02 — Observable & Supervised Agent

## Overview
This project introduces an **observable, supervised LangGraph agent** designed with production-style concerns in mind.

Unlike the tool-calling agent in Project 01, this project focuses on **control, visibility, and reliability** rather than just correct execution.

The agent is treated as a **system**, not a script.

---

## 🎯 Goal
The goal of this project is to build an agent that:

- Executes tasks through a worker agent  
- Is overseen by a supervisor agent  
- Makes routing decisions based on confidence and state  
- Emits structured logs and metrics for observability  
- Handles failures explicitly and predictably  

---

## 🧠 Key Concepts Introduced
This project intentionally introduces **new system-level concepts**, without repeating Project 01 logic.

### New Concepts
- Supervisor–Worker agent pattern  
- Confidence-based routing and termination  
- Observability-first design (logs, metrics, events)  
- Explicit failure detection and recovery  
- State transitions as first-class signals  

### Concepts Carried Forward
- State-driven agent architecture  
- Deterministic tool execution  
- Explicit routing logic  
- Guarded termination  

---

## 🏗️ High-Level Architecture

The agent is composed of **clearly separated control-plane components**.

### Logical Components
- **Supervisor Agent**
  - Evaluates worker output
  - Decides `SUCCESS`, `RETRY`, or `FAILURE`
  - Owns final system status
- **Worker Agent**
  - Executes deterministic tools
  - Produces factual output
  - Derives confidence scores
- **Router**
  - Maps supervisor decisions to the next node
  - Contains no business logic
- **Observability Layer**
  - Emits structured logs and metrics
  - Tracks retries, failures, and outcomes
- **Shared State**
  - Single source of truth
  - Passed through every node

---

## 🔁 Control Flow Diagram

The system follows a **supervised loop with bounded retries**.

                            ┌────────────────────┐
                            │        START       │
                            │  (initialize state)│
                            └─────────┬──────────┘
                                      │
                                      ▼
                            ┌────────────────────┐
                            │       WORKER       │
                            │  - Execute tool    │
                            │  - Produce output  │
                            │  - Derive confidence
                            └─────────┬──────────┘
                                      │
                                      ▼
                            ┌────────────────────┐
                            │     SUPERVISOR     │
                            │  - Evaluate state  │
                            │  - Decide outcome  │
                            │    • SUCCESS       │
                            │    • RETRY         │
                            │    • FAILURE       │
                            └─────────┬──────────┘
                                      │
                                      ▼
                            ┌────────────────────┐
                            │       ROUTER       │
                            │  Map decision →    │
                            │  next execution    │
                            └──────┬───────┬─────┘
                                  │       │
                                  │       │
                                  │       ▼
                                  │  ┌─────────────────┐
                                  │  │   END_FAILURE   │
                                  │  │  (safe stop)    │
                                  │  └─────────────────┘
                                  │
                                  ▼
                            ┌────────────────────┐
                            │  RETRY PATH        │
                            │  - Increment retry │
                            │  - Check max limit │
                            └─────────┬──────────┘
                                      │
                                      ▼
                                (back to WORKER)
    
    This loop continues until the supervisor emits a terminal decision (`SUCCESS` or `FAILURE`).



### Decision Semantics
- `RETRY` → loop back to worker (retry count increments)
- `SUCCESS` → terminate successfully
- `FAILURE` → terminate safely after retry exhaustion

---

## 🚨 Failure-Aware by Design

Failure is treated as a **normal system outcome**, not an exception.

The agent explicitly handles:
- Low-confidence outputs  
- Tool execution failures  
- Invalid inputs  
- Retry exhaustion  
- Safe termination  

Failures are:
- Logged  
- Counted  
- Recorded in state  
- Used for control decisions  

Failure strategies are documented in `docs/failure-modes.md`.

---

## 🧩 Project Rules
- No hidden control flow  
- All routing decisions must be explainable  
- Observability is not optional  
- Failures must be detectable and actionable  
- Each component has a single responsibility  

---

## 📚 Learning Outcome
By completing this project, you should be able to:

- Design supervised agent systems  
- Reason about agent failures before they occur  
- Instrument agents for debugging and monitoring  
- Explain agent behavior step-by-step  
- Justify architectural decisions in interviews  

---

## 🔒 Project Status
✅ **Complete (learning milestone)**  
📌 Scoped for learning, not production deployment  

This project is frozen as a **reference implementation**.

---

## 🔁 Relation to Other Projects
- **Project 01** — Tool-calling & looping agents  
- **Project 02** — Supervision, observability, and safe termination  
- **Future projects** — Concurrency, human-in-the-loop, multi-agent systems  

---

## 🧠 Final Note
This project reflects a deliberate shift in mindset:

> From *“Can the agent do the task?”*  
> To *“Can I trust, observe, and control the agent?”*
