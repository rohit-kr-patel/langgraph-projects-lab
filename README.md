# LangGraph Project Lab

A **project-based learning repository** for building, experimenting with, and evolving **AI agents using LangGraph**.

This repository follows a **step-by-step learning journey**, where each numbered folder represents a distinct milestone in understanding agent architectures, state management, routing, supervision, observability, and human-in-the-loop workflows.

This is **not a tutorial repository**.
This is **learning by building real systems**.

---

# 🎯 Purpose

The goal of this repository is to:

* Learn **LangGraph through hands-on projects**
* Understand how agent workflows are modeled as **state machines**
* Build confidence with **StateGraph design patterns**
* Explore routing, supervision, retries, and human intervention
* Practice designing **safe, observable, and controllable AI systems**
* Progress from simple agents to production-inspired architectures

---

# 🧠 Learning Philosophy

This repository follows a few core principles:

* Learn by building
* One project, one concept
* Explicit control flow over hidden abstractions
* Small projects before large systems
* Incremental complexity
* Reliability before optimization

Each project focuses on a specific architectural concept and introduces only a small number of new ideas.

---

# 📂 Repository Structure

```text
langgraph-projects-lab/
│
├── 01-tool-calling-agent/
├── 02-observable-supervised-agent/
├── 03-human-in-the-loop-agent/
│
└── README.md
```

### Folder Convention

* Numbered folders (`01`, `02`, `03`, ...)
* Each folder is a standalone project
* Projects remain unchanged after completion
* New concepts are introduced only in newer projects
* Earlier projects serve as learning references

This approach preserves architectural history and learning progression.

---

# 🧩 Projects

---

## 01 - Tool Calling Agent

### Goal

Build an agent capable of reasoning and interacting with external tools.

### Concepts Covered

* LangGraph fundamentals
* StateGraph basics
* Tool integration
* Agent → Tool → Agent loops
* Deterministic execution
* State updates
* Loop termination

### Key Learning

This project introduces the transition from passive LLM interactions to action-oriented agents that can use tools to accomplish tasks.

---

## 02 - Observable & Supervised Agent

### Goal

Build a supervised agent with explicit control flow and observability.

### Concepts Covered

* Supervisor–Worker architecture
* Confidence-based routing
* Agent observability
* Event tracking
* Retry mechanisms
* Failure handling
* Safe workflow termination

### Key Learning

This project treats agents as systems rather than scripts and introduces production-style concerns such as monitoring, control, and reliability.

---

## 03 - Human-in-the-Loop Agent

### Goal

Build a workflow that combines automation with human oversight using LangGraph's Human-in-the-Loop capabilities.

### Concepts Covered

* Human-in-the-Loop (HITL)
* LangGraph `interrupt()`
* Workflow pause and resume
* Checkpointing with MemorySaver
* Human approval workflows
* Conditional routing
* Shared workflow state
* Audit history

### Project Scenario

A loan approval workflow where:

1. Automation evaluates loan risk.
2. Supervisor evaluates confidence.
3. High-confidence decisions are automatically approved.
4. Low-confidence decisions require human review.
5. Workflow pauses using `interrupt()`.
6. Human provides a decision.
7. Workflow resumes from the exact interruption point.

### Workflow Architecture

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
```

### Key Learning

This project introduces one of LangGraph's most powerful features: the ability to pause execution, wait for human intervention, and resume execution later while preserving workflow state.

---

# 🧩 Project Rules

Every project in this repository follows the same architectural principles:

* Explicit graph design
* Deterministic execution
* Explainable routing decisions
* State-driven workflows
* Clear failure handling
* No hidden control flow
* Minimal magic
* Reproducible behavior

---

# 🏗 Architectural Themes

As projects progress, the repository explores:

### State Management

* Shared workflow state
* State transitions
* State validation
* State persistence

### Routing

* Conditional edges
* Dynamic decision making
* Confidence-based control flow

### Reliability

* Failure handling
* Retry strategies
* Safe termination

### Observability

* Audit history
* Logging
* Execution tracking
* Decision transparency

### Human Oversight

* Approval workflows
* Human intervention
* Workflow interruption
* Workflow resumption

---

# 🚀 When to Create a Separate Repository

A project graduates from this lab into its own repository when:

* It solves a focused problem
* It has a stable architecture
* It is production-ready or showcase-ready
* It can evolve independently
* It no longer benefits from the learning-lab structure

Until then, all experiments remain here.

---

# 🛠 Tech Stack

* Python
* LangGraph
* LangChain
* StateGraph
* Dataclasses
* Async-first architecture
* Human-in-the-Loop workflows

---

# 📚 Current Learning Roadmap

```text
01 → Tool Calling Agent
        ↓
02 → Observable & Supervised Agent
        ↓
03 → Human-in-the-Loop Agent
        ↓
04 → Multi-Agent Systems (Planned)
        ↓
05 → Production Agent Architectures (Planned)
```

---

# 📈 Status

* 🚧 Active Learning Repository
* 🧪 Experimental Projects
* 📚 Focused on Agent Fundamentals
* 🔄 Continuously Evolving

---

# 🧠 Final Note

This repository reflects a systems-oriented approach to building AI agents.

Agents are treated as:

* Systems, not scripts
* State machines, not chatbots
* Workflows, not prompts
* Products in evolution, not demos

The objective is not just to learn LangGraph APIs, but to understand how trustworthy, observable, controllable, and production-ready agent systems are designed.

Every project is a deliberate step toward building reliable AI applications.
