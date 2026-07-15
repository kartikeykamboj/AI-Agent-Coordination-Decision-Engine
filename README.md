# AI Agent Coordination & Decision Engine

> Infosys Springboard Virtual Internship 7.0
> **Milestone 1 – Multi-Agent Foundation Development**

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-success?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Passing-brightgreen?style=for-the-badge&logo=githubactions)

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
- Build Coordinator and Workflow Orchestrator
- Develop specialized Planner, Research and Decision Agents
- Implement intelligent multi-agent routing
- Integrate Google Gemini LLM
- Implement short-term memory management
- Establish enterprise-ready project architecture
- Create unit testing framework
- Configure GitHub Actions CI pipeline
- Prepare project documentation

---

# Features Implemented

- Workflow Orchestrator
- Coordinator Agent
- Planner Agent
- Research Agent
- Decision Agent
- Intelligent Multi-Agent Routing
- Prompt Template Management
- Gemini API Integration
- LangChain Integration
- Memory Manager (Short-Term Memory)
- Enterprise Modular Architecture
- Unit Test Framework (Pytest)
- GitHub Actions Continuous Integration
- Comprehensive Project Documentation
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
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
 Research Agent   Planner Agent   Decision Agent
      │                │                │
      └────────────────┼────────────────┘
                       ▼
             Prompt Engineering Layer
                       │
                       ▼
             Google Gemini LLM
                       │
                       ▼
                Memory Manager
                       │
                       ▼
                Final Response
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
│   │   ├── coordinator.py
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   └── decision_agent.py
│   ├── memory/
│   ├── prompts/
│   ├── tools/
│   ├── workflow/
│   │   └── orchestrator.py
│   └── app.py
│
├── tests/
│
├── CHANGELOG.md
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
- Multi-Agent Architecture
- Workflow Orchestration
- Memory Management
- Git & GitHub
- GitHub Actions
- VS Code
- Pytest

---

# Workflow

1. User submits a request.
2. Workflow Orchestrator receives the request.
3. Coordinator Agent analyses the request.
4. Coordinator intelligently routes the request to the appropriate specialized AI agent.
5. Planner, Research or Decision Agent processes the task.
6. Prompt Template prepares the instruction.
7. Google Gemini LLM generates the response.
8. Memory Manager stores the interaction.
9. Final response is returned to the user.

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

- Agent-to-Agent Communication
- Tool Calling
- REST API Integration
- Vector Database Memory
- Long-Term Memory
- Retrieval-Augmented Generation (RAG)
- Enterprise Workflow Automation
- Dashboard & Monitoring
- Authentication & Role-Based Access
- External API Integrations

---

# Internship Mapping

| Milestone Requirement   | Status      |
| ----------------------- | ----------- |
| LangChain Configuration | ✅ Completed |
| Foundational AI Agents  | ✅ Completed |
| Prompt Templates        | ✅ Completed |
| Workflow Orchestrator   | ✅ Completed |
| Coordinator Agent       | ✅ Completed |
| Planner Agent           | ✅ Completed |
| Research Agent          | ✅ Completed |
| Decision Agent          | ✅ Completed |
| Multi-Agent Routing     | ✅ Completed |
| Memory Foundation       | ✅ Completed |
| Testing Framework       | ✅ Completed |
| GitHub Actions CI       | ✅ Completed |
| Documentation           | ✅ Completed |


---

# Repository Status

**Current Phase:** Milestone 1 successfully completed.

The project includes a Workflow Orchestrator, Coordinator Agent, Planner Agent, Research Agent, Decision Agent, intelligent multi-agent routing, LangChain integration, Google Gemini API integration, Memory Manager, unit testing framework, GitHub Actions CI pipeline, and comprehensive project documentation.

The repository establishes a scalable enterprise-ready architecture for future multi-agent collaboration, tool integration, and intelligent workflow automation.

---

# Author

**Kartikey Kamboj**

Intern

Infosys Springboard Virtual Internship 7.0

---

# License

This project is licensed under the **MIT License**.