from prompts.coordinator_prompt import coordinator_prompt
from tools.tools import llm


class ResearchAgent:
    def __init__(self):
        self.chain = coordinator_prompt | llm

    def run(self, query: str):

        prompt = f"""
You are an AI Research Agent.

Your responsibility is to:

- Research the given topic.
- Explain technical concepts.
- Gather useful information.
- Respond professionally.

Topic:

{query}
"""

        response = self.chain.invoke({"input": prompt})

        if hasattr(response, "text"):
            return response.text

        return str(response)