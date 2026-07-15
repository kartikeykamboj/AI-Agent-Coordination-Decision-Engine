from agents.coordinator import CoordinatorAgent
from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.decision_agent import DecisionAgent
from memory.memory import MemoryManager


class WorkflowOrchestrator:
    """
    AI Workflow Orchestrator

    Routes requests to specialized AI agents.
    """

    def __init__(self):
        self.coordinator = CoordinatorAgent()
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.decision = DecisionAgent()
        self.memory = MemoryManager()

    def execute(self, user_request):

        query = user_request.lower()

        if any(word in query for word in ["plan", "roadmap", "steps", "workflow"]):
            response = self.planner.run(user_request)

        elif any(word in query for word in ["what is", "explain", "research", "information"]):
            response = self.researcher.run(user_request)

        elif any(word in query for word in ["should", "recommend", "best", "choose", "decision"]):
            response = self.decision.run(user_request)

        else:
            response = self.coordinator.run(user_request)

        self.memory.add(user_request, response)

        return response

    def get_history(self):
        return self.memory.get_history()