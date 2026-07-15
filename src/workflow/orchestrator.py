from agents.coordinator import CoordinatorAgent
from memory.memory import MemoryManager


class WorkflowOrchestrator:
    """
    Central AI Workflow Orchestrator

    Responsible for:

    - Receiving requests
    - Invoking Coordinator Agent
    - Managing conversation memory
    - Returning final response
    """

    def __init__(self):
        self.coordinator = CoordinatorAgent()
        self.memory = MemoryManager()

    def execute(self, user_request):

        response = self.coordinator.run(user_request)

        self.memory.add(user_request, response)

        return response

    def get_history(self):
        return self.memory.get_history()