from prompts.coordinator_prompt import coordinator_prompt
from tools.tools import llm


class PlannerAgent:
    def __init__(self):
        self.chain = coordinator_prompt | llm

    def run(self, task: str):

        prompt = f"""
You are an AI Planning Agent.

Your job is to:

- Break large tasks into smaller steps.
- Create execution plans.
- Recommend workflow.
- Return the answer clearly.

Task:

{task}
"""

        response = self.chain.invoke({"input": prompt})

        if hasattr(response, "text"):
            return response.text

        return str(response)