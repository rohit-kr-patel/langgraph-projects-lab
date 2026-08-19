# LangGraph Project Lab

A **project-based learning repository** for building, experimenting with, and evolving **AI agents using LangGraph**.

This repository follows a **step-by-step learning journey**, where each numbered folder represents a distinct milestone in understanding agent architectures, state management, routing, supervision, observability, human-in-the-loop workflows, and multi-agent systems.

This is **not a tutorial repository**.  
This is **learning by building real systems**.

---

# 🎯 Purpose

The goal of this repository is to:

- Learn **LangGraph through hands-on projects**
- Understand how agent workflows are modeled as **state machines**
- Build confidence with **StateGraph design patterns**
- Explore routing, supervision, retries, and human intervention
- Learn multi-agent orchestration patterns
- Practice designing **safe, observable, and controllable AI systems**
- Progress from simple agents to production-inspired architectures

---

# 🧠 Learning Philosophy

This repository follows a few core principles:

- Learn by building
- One project, one concept
- Explicit control flow over hidden abstractions
- Small projects before large systems
- Incremental complexity
- Reliability before optimization

Each project focuses on a specific architectural concept and introduces only a small number of new ideas.

---

# 📂 Repository Structure

```text
langgraph-projects-lab/
│
├── 01-tool-calling-agent/
├── 02-observable-supervised-agent/
├── 03-human-in-the-loop-agent/
├── 04-multi-agent-research-assistant/
│
└── README.md
```

### Folder Convention

- Numbered folders (`01`, `02`, `03`, ...)
- Each folder is a standalone project
- Projects remain unchanged after completion
- New concepts are introduced only in newer projects
- Earlier projects serve as learning references

This approach preserves architectural history and learning progression.

---

# 🧩 Projects

---

## 01 - Tool Calling Agent

### Goal

Build an agent capable of reasoning and interacting with external tools.

### Concepts Covered

- LangGraph fundamentals
- StateGraph basics
- Tool integration
- Agent → Tool → Agent loops
- Deterministic execution
- State updates
- Loop termination

### Key Learning

This project introduces the transition from passive LLM interactions to action-oriented agents that can use tools to accomplish tasks.

---

## 02 - Observable & Supervised Agent

### Goal

Build a supervised agent with explicit control flow and observability.

### Concepts Covered

- Supervisor–Worker architecture
- Confidence-based routing
- Agent observability
- Event tracking
- Retry mechanisms
- Failure handling
- Safe workflow termination

### Key Learning

This project treats agents as systems rather than scripts and introduces production-style concerns such as monitoring, control, and reliability.

---

## 03 - Human-in-the-Loop Agent

### Goal

Build a workflow that combines automation with human oversight using LangGraph's Human-in-the-Loop capabilities.

### Concepts Covered

- Human-in-the-Loop (HITL)
- LangGraph `interrupt()`
- Workflow pause and resume
- Checkpointing with MemorySaver
- Human approval workflows
- Conditional routing
- Shared workflow state
- Audit history

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

This project introduces one of LangGraph's most powerful capabilities: pausing execution, waiting for human intervention, and resuming execution later while preserving workflow state.

---

## 04 - Multi-Agent Research Assistant 🚧

### Goal

Build a supervisor-driven multi-agent system where specialized agents collaborate to research, verify, and summarize information.

### Concepts Covered

- Multi-Agent Architectures
- Agent Specialization
- Shared State Communication
- Agent Handoffs
- Supervisor-Based Orchestration
- Sequential Agent Workflows
- LLM-Powered Agents
- Groq Integration
- Research Pipelines

### Planned Agents

```text
Supervisor Agent
        │
        ├── Research Agent
        ├── Fact Checker Agent
        └── Summarizer Agent
```

### Workflow Architecture

```text
START
  │
  ▼
Supervisor
  │
  ▼
Research Agent
  │
  ▼
Supervisor
  │
  ▼
Fact Checker Agent
  │
  ▼
Supervisor
  │
  ▼
Summarizer Agent
  │
  ▼
Supervisor
  │
  ▼
END
```

### Shared State

```python
@dataclass
class ResearchState:
    query: str

    research_notes: str = ""

    verified_notes: str = ""

    final_answer: str = ""

    next_agent: str = ""

    history: list[str] = field(default_factory=list)
```

### Current Progress

#### Day 1 ✅

- Designed shared state model
- Defined agent responsibilities
- Designed workflow architecture

#### Day 2 ✅

- Integrated Groq API
- Built reusable LLM layer
- Verified LLM connectivity

#### Upcoming

- Research Agent
- Fact Checker Agent
- Summarizer Agent
- Supervisor Routing
- Graph Orchestration
- End-to-End Workflow

### Key Learning

This project introduces the transition from single-agent workflows to coordinated multi-agent systems where specialized agents collaborate through shared state under the control of a supervisor.

---

# 🧩 Project Rules

Every project in this repository follows the same architectural principles:

- Explicit graph design
- Deterministic execution
- Explainable routing decisions
- State-driven workflows
- Clear failure handling
- Minimal hidden behavior
- Reproducible execution
- Incremental complexity

---

# 🏗 Architectural Themes

As projects progress, the repository explores:

## State Management

- Shared workflow state
- State transitions
- State validation
- State persistence

## Routing

- Conditional edges
- Dynamic decision making
- Confidence-based control flow
- Supervisor orchestration

## Reliability

- Failure handling
- Retry strategies
- Safe termination

## Observability

- Audit history
- Logging
- Execution tracking
- Decision transparency

## Human Oversight

- Approval workflows
- Human intervention
- Workflow interruption
- Workflow resumption

## Multi-Agent Systems

- Agent specialization
- Agent handoffs
- Shared memory
- Supervisor-driven coordination
- Collaborative reasoning

---

# 🚀 When to Create a Separate Repository

A project graduates from this lab into its own repository when:

- It solves a focused problem
- It has a stable architecture
- It is production-ready or showcase-ready
- It can evolve independently
- It no longer benefits from the learning-lab structure

Until then, all experiments remain here.

---

# 🛠 Tech Stack

- Python
- LangGraph
- LangChain
- StateGraph
- Dataclasses
- Groq API
- Human-in-the-Loop Workflows
- Multi-Agent Architectures

---

# 📚 Current Learning Roadmap

```text
01 → Tool Calling Agent                         ✅
        ↓
02 → Observable & Supervised Agent             ✅
        ↓
03 → Human-in-the-Loop Agent                   ✅
        ↓
04 → Multi-Agent Research Assistant            🚧
        ↓
05 → Planner–Executor Agent                    🔜
        ↓
06 → RAG Agent                                 🔜
        ↓
07 → Long-Term Memory Agent                    🔜
        ↓
08 → Production Agent Architectures            🔜
```

---

# 📈 Status

- 🚧 Active Learning Repository
- 🧪 Experimental Projects
- 📚 Focused on Agent Fundamentals
- 🔄 Continuously Evolving

### Current Progress

```text
Projects Completed : 3
Project In Progress: 1
Current Focus      : Multi-Agent Systems
```

---

# 🧠 Final Note

This repository reflects a systems-oriented approach to building AI agents.

Agents are treated as:

- Systems, not scripts
- State machines, not chatbots
- Workflows, not prompts
- Products in evolution, not demos

The objective is not just to learn LangGraph APIs, but to understand how trustworthy, observable, controllable, and production-ready agent systems are designed.

Every project is a deliberate step toward building reliable AI applications.