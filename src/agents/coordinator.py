from prompts.coordinator_prompt import coordinator_prompt
from tools.tools import llm


class CoordinatorAgent:
    def __init__(self):
        self.chain = coordinator_prompt | llm

    def run(self, user_input: str) -> str:
        print("\n" + "=" * 50)
        print(" Coordinator Agent Activated ")
        print("=" * 50)
        print(f"User Request: {user_input}")
        print("-" * 50)

        response = self.chain.invoke({"input": user_input})

        if hasattr(response, "text") and response.text:
            print("Response Generated Successfully")
            print("=" * 50)
            return response.text

        if hasattr(response, "content"):
            if isinstance(response.content, str):
                print("Response Generated Successfully")
                print("=" * 50)
                return response.content

            if isinstance(response.content, list):
                output = []

                for item in response.content:
                    if isinstance(item, dict):
                        if item.get("type") == "text":
                            output.append(item.get("text", ""))

                print("Response Generated Successfully")
                print("=" * 50)
                return "\n".join(output)

        return str(response)