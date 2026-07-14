# System Architecture

## High-Level Architecture

```text
                   User
                     │
                     ▼
           Coordinator Agent
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
Planner Agent  Retrieval Agent  Decision Agent
     │               │                │
     └───────────────┼────────────────┘
                     ▼
            Execution Agent
                     │
                     ▼
            Response Generator
                     │
                     ▼
                   User
```

---

## Agent Responsibilities

### Coordinator Agent

Responsible for managing communication between all AI agents.

---

### Planner Agent

Breaks user requests into smaller executable tasks.

---

### Retrieval Agent

Collects relevant information from available knowledge sources and APIs.

---

### Decision Agent

Evaluates retrieved information and recommends optimal actions.

---

### Execution Agent

Executes tasks, coordinates workflow execution, and validates outputs.

---

### Response Generator

Produces the final response returned to the user.

---

## Technologies Used

- LangChain
- LangGraph
- Gemini API
- Python
- FastAPI

---

## Future Enhancements

- Memory Integration
- RAG Pipeline
- Multi-LLM Support
- Human-in-the-loop Approval
- Dashboard
