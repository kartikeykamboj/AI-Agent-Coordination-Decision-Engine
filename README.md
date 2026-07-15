# AI Agent Coordination & Decision Engine

> Infosys Springboard Virtual Internship 7.0  
> Milestone 1 - Agent Foundation Development

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-success?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

# Project Overview

Modern enterprises increasingly rely on AI-powered systems to automate business processes, analyze information, coordinate specialized AI agents, and support intelligent decision-making.

This project aims to develop an **AI Agent Coordination & Decision Engine** capable of coordinating multiple AI agents to collaboratively solve enterprise-level tasks using Large Language Models (LLMs), workflow orchestration, memory systems, and tool integration.

This repository contains the implementation completed during **Milestone 1** of the Infosys Springboard Virtual Internship.

---

# Milestone 1 Objectives

- Configure LangChain and required dependencies
- Develop foundational AI agents
- Implement prompt templates
- Build coordinator and orchestration workflow
- Integrate Gemini LLM
- Establish project architecture
- Create testing framework
- Prepare project documentation

---

# Features Implemented

- Coordinator Agent
- Workflow Orchestrator
- Prompt Template Management
- Gemini API Integration
- LangChain Integration
- Memory Manager (Short-Term Memory)
- Modular Project Structure
- Unit Test Framework
- GitHub Actions Workflow
- MIT Licensed Repository

---

# Current Architecture

```text
                User
                  │
                  ▼
        Workflow Orchestrator
                  │
                  ▼
         Coordinator Agent
                  │
        Prompt Engineering Layer
                  │
                  ▼
          Gemini Large Language Model
                  │
                  ▼
         Response Generation Engine
                  │
                  ▼
          Memory Management Layer
```

---

# Project Structure

```text
AI-Agent-Coordination-Decision-Engine

├── .github/
│   └── workflows/
│
├── docs/
│   ├── Agile/
│   ├── Architecture/
│   ├── Defect-Tracker/
│   ├── Milestones/
│   └── Unit-Test-Plan/
│
├── src/
│   ├── agents/
│   ├── memory/
│   ├── prompts/
│   ├── tools/
│   ├── workflow/
│   └── app.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# Technologies Used

- Python
- LangChain
- Google Gemini API
- Prompt Engineering
- Git & GitHub
- GitHub Actions
- VS Code
- Pytest

---

# Workflow

1. User submits a request.
2. Workflow Orchestrator receives the request.
3. Coordinator Agent analyzes the task.
4. Prompt Template prepares the instruction.
5. Gemini LLM generates the response.
6. Memory Manager stores the interaction.
7. Final response is returned to the user.

---

# Setup Instructions

Clone the repository

```bash
git clone https://github.com/kartikeykamboj/AI-Agent-Coordination-Decision-Engine.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python src/app.py
```

---

# Testing

Run unit tests

```bash
pytest
```

---

# Future Enhancements

- Multi-Agent Collaboration
- Planner Agent
- Research Agent
- Decision Support Agent
- Tool Calling
- REST API Integration
- Vector Database Memory
- Enterprise Workflow Automation
- Dashboard & Monitoring
- Multi-Agent Communication

---

# Internship Mapping

| Milestone Requirement | Status |
|-----------------------|--------|
| LangChain Configuration | ✅ Completed |
| Foundational Agent | ✅ Completed |
| Prompt Templates | ✅ Completed |
| Testing Framework | ✅ Completed |
| Coordinator Agent | ✅ Completed |
| Workflow Orchestration | ✅ Completed |
| Memory Foundation | ✅ Completed |

---

# Repository Status

**Current Phase:** Milestone 1 completed (foundation) with a working Coordinator Agent, Workflow Orchestrator, LangChain integration, and Gemini-powered response generation.

The project establishes a modular enterprise-ready architecture for developing collaborative AI agent ecosystems.

---

# Author

**Kartikey Kamboj**

B.Tech Computer Science Engineering (Twinning)

Infosys Springboard Virtual Internship 7.0

---

# License

This project is licensed under the **MIT License**.