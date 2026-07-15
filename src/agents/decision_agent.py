from prompts.coordinator_prompt import coordinator_prompt
from tools.tools import llm


class DecisionAgent:
    def __init__(self):
        self.chain = coordinator_prompt | llm

    def run(self, problem: str):

        prompt = f"""
You are an Enterprise Decision Support Agent.

Your job is to:

- Analyse available options.
- Compare advantages and disadvantages.
- Recommend the best decision.
- Explain your reasoning.

Problem:

{problem}
"""

        response = self.chain.invoke({"input": problem})

        if hasattr(response, "text"):
            return response.text

        return str(response)