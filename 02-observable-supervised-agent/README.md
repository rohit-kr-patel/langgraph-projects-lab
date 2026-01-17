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
This project intentionally introduces **new concepts only**, without repeating Project 01 logic.

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
The system is composed of the following logical components:

- **Supervisor Agent**
  - Interprets task progress
  - Decides whether to continue, retry, or terminate
- **Worker Agent**
  - Performs task execution
- **Router**
  - Directs control flow based on confidence and state
- **Observability Layer**
  - Logs decisions, transitions, and failures
  - Tracks execution metrics
- **Shared State**
  - Single source of truth for agent behavior

Detailed architecture is documented in `docs/architecture.md`.

---

## 🚨 Failure-Aware by Design
Failure is treated as a **normal system outcome**, not an exception.

This project explicitly handles:
- Low-confidence LLM outputs  
- Partial task completion  
- Tool execution failures  
- Retry exhaustion  
- Safe termination conditions  

Failure handling strategies are documented in `docs/failure-modes.md`.

---

## 🧩 Project Rules
- No hidden control flow  
- All routing decisions must be explainable  
- Observability is not optional  
- Failures must be detectable and actionable  
- Each component must have a clear responsibility  

---

## 📚 Learning Outcome
By completing this project, you should be able to:

- Design supervised agent systems  
- Reason about agent failures before they occur  
- Instrument agents for debugging and monitoring  
- Explain agent behavior step-by-step  
- Decide when advanced agent frameworks are justified  

---

## 🔒 Project Status
🚧 In progress  
📌 Scoped for learning, not production deployment  

---

## 🔁 Relation to Other Projects
- **Project 01** introduced tool-calling and looping agents  
- **Project 02** builds on that foundation by adding supervision and observability  
- Future projects will introduce scalability, concurrency, and human-in-the-loop patterns  

---

## 🧠 Final Note
This project reflects a deliberate shift in mindset:

> From *“Can the agent do the task?”*  
> To *“Can I trust, observe, and control the agent?”*
