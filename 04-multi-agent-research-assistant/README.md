# 04 - Multi-Agent Research Assistant

A LangGraph project focused on learning how multiple AI agents collaborate through a shared state under the control of a supervisor.

This project introduces the concept of **multi-agent systems**, where specialized agents perform different tasks and pass information to each other through a common workflow state.

---

# 🎯 Goal

Build a supervisor-driven research workflow that:

1. Researches a topic
2. Verifies the research
3. Summarizes the verified information
4. Returns a final answer

The focus is on understanding:

- Agent specialization
- Shared state communication
- Agent handoffs
- Supervisor orchestration
- Multi-agent workflow design

---

# 🧠 Learning Objectives

By the end of this project, you should understand:

- How multiple agents collaborate
- How agents communicate using shared state
- How supervisors coordinate workflows
- How LangGraph enables agent orchestration
- How to design scalable multi-agent architectures
- How LLM-powered agents can be composed into larger systems

---

# 🏗 Architecture

```text
                    Supervisor
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 Research Agent   Fact Checker Agent   Summarizer Agent
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
                    Final Answer
```

---

# 🔄 Workflow

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

---

# 🤖 Agents

## Research Agent

### Responsibility

Gather information related to the user's query.

### Input

```python
state.query
```

### Output

```python
state.research_notes
```

---

## Fact Checker Agent

### Responsibility

Review and validate research findings.

### Input

```python
state.research_notes
```

### Output

```python
state.verified_notes
```

---

## Summarizer Agent

### Responsibility

Generate a concise final response.

### Input

```python
state.verified_notes
```

### Output

```python
state.final_answer
```

---

## Supervisor Agent

### Responsibility

Coordinate the workflow and decide which agent should run next.

The supervisor never performs research itself.

It only manages workflow progression.

---

# 📦 Shared State

The workflow uses a single shared state object.

```python
from dataclasses import dataclass, field

@dataclass
class ResearchState:
    query: str

    research_notes: str = ""

    verified_notes: str = ""

    final_answer: str = ""

    next_agent: str = ""

    history: list[str] = field(default_factory=list)
```

---

# 🔁 State Flow

```text
User Query
     │
     ▼
query
     │
     ▼
Research Agent
     │
     ▼
research_notes
     │
     ▼
Fact Checker Agent
     │
     ▼
verified_notes
     │
     ▼
Summarizer Agent
     │
     ▼
final_answer
```

---

# 🛠 Tech Stack

- Python
- LangGraph
- StateGraph
- Groq API
- Dataclasses
- dotenv

---

# 📂 Project Structure

```text
04-multi-agent-research-assistant/
│
├── app.py
├── graph.py
├── nodes.py
├── state.py
├── llm.py
├── .env
├── requirements.txt
│
└── README.md
```

---

# 📅 Development Progress

## Day 1 ✅

### State Design

Completed:

- Designed shared workflow state
- Defined agent responsibilities
- Defined data flow between agents
- Designed overall architecture

---

## Day 2 ✅

### LLM Integration

Completed:

- Setup Groq API
- Built reusable LLM wrapper
- Configured environment variables
- Verified model connectivity

---

## Day 3 ✅

Completed:

- Implement Research Agent
- Generate research notes
- Update shared state

---

## Day 4 ⏳

Planned:

- Implement Fact Checker Agent
- Validate research output

---

## Day 5 ⏳

Planned:

- Implement Summarizer Agent
- Generate final answer

---

## Day 6 ⏳

Planned:

- Build Supervisor Node
- Add routing logic

---

## Day 7 ⏳

Planned:

- Build LangGraph workflow
- Connect all agents
- End-to-end testing

---

# 🎓 Key Concept Introduced

This project introduces:

> Multi-Agent Collaboration

Instead of one agent doing everything, multiple specialized agents work together through shared state while a supervisor coordinates execution.

This is a foundational pattern for building scalable AI systems.

---

# 🚀 Future Enhancements

Possible future extensions:

- Tool-enabled research agents
- Web search integration
- Human-in-the-loop verification
- Agent memory
- Parallel agent execution
- Multi-step planning
- Production API deployment

---

# 🧠 Final Note

This project marks the transition from single-agent workflows to coordinated multi-agent systems.

The primary objective is not just generating answers, but understanding how multiple agents communicate, collaborate, and complete tasks through structured workflows.

It serves as the foundation for more advanced architectures such as planner-executor systems, RAG agents, and production-grade AI orchestration platforms.