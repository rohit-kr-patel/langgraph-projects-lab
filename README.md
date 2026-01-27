# LangGraph Project Lab

A **project-based learning repository** for building and evolving **AI agents using LangGraph**.

This repository follows a **step-by-step project approach**, where each numbered folder represents a clear learning milestone in agent design, control flow, and system thinking.

This is **not a tutorial repo**.  
This is **learning by building**.

---

## 🎯 Purpose

The goal of this repository is to:

- Learn **LangGraph by building real projects**
- Understand agent **state, routing, looping, and termination**
- Practice designing **safe and reliable agent workflows**
- Move from simple agents to **production-style architectures**
- Develop strong fundamentals for **agent-based systems**

---

## 🧠 Learning Philosophy

- One repository for **structured learning**
- Projects are **incremental and ordered**
- Each project focuses on **specific LangGraph concepts**
- Complexity increases gradually
- **Clarity > cleverness**

---

## 📂 Folder Convention

- **Numbered folders (`01`, `02`, …)** show learning progression
- Each folder represents a **standalone LangGraph project**
- Earlier projects remain **unchanged once completed**
- New concepts are introduced **only in newer projects**

This enforces architectural discipline and prevents regressions.

---

## 🧩 Projects

### `01_tool_calling_agent`
**Goal:** Build an agent that can think and act using tools.

**Focus:**
- LLM-driven tool selection
- Deterministic tool execution
- Agent → Tool → Agent looping
- State updates after tool calls
- Guarding against infinite loops

This project introduces **core LangGraph behavior** and represents the transition from passive agents to **action-oriented agents**.

---

### `02_observable_supervised_agent`
**Goal:** Build a supervised, observable agent with explicit control flow.

**Focus:**
- Supervisor–Worker agent pattern
- Confidence-based routing and termination
- Observability-first design (logs, metrics, events)
- Explicit failure handling and recovery
- Bounded retries and safe termination

This project treats the agent as a **system**, not a script, and introduces **production-style control and reliability concerns**.

---

## 🧩 Project Rules

For every project in this repository:

- Graph logic must be **explicit**
- Tools must be **deterministic**
- Routing decisions must be **explainable**
- No hidden magic or shortcuts
- Each project must stand on its own

---

## 🚀 When to Create a New Repository

A project is moved into its **own repository** only when:

- It solves a single, well-defined problem
- It can be used independently
- It is stable and showcase-ready
- It no longer benefits from the lab structure

Until then, everything lives here.

---

## 🛠 Tech Stack

- Python
- LangGraph
- LangChain
- Async-first design
- State-driven agent architecture

---

## 📈 Status

🚧 Active learning  
📚 Focused on fundamentals  
🧪 Iterative and experimental  

---

## 🧠 Final Note

This repository reflects **how I approach agent systems**:

Agents are treated as:
- **Systems**, not scripts
- **State machines**, not chatbots
- **Products in evolution**, not demos

Each project is a deliberate step toward building **trustworthy, controllable AI agents**.
