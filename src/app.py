from workflow.orchestrator import WorkflowOrchestrator


def print_banner():
    print("=" * 65)
    print("      AI Agent Coordination & Decision Engine")
    print("      Infosys Springboard Virtual Internship 7.0")
    print("      Milestone 1 - Multi-Agent Prototype")
    print("=" * 65)


def main():
    print_banner()

    orchestrator = WorkflowOrchestrator()

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nSession Ended. Thank you!")
            break

        query = user_input.lower()

        if any(word in query for word in ["plan", "roadmap", "steps", "workflow"]):
            print("\n>>> Planner Agent Selected\n")

        elif any(word in query for word in ["what is", "explain", "research", "information"]):
            print("\n>>> Research Agent Selected\n")

        elif any(word in query for word in ["should", "recommend", "best", "choose", "decision"]):
            print("\n>>> Decision Agent Selected\n")

        else:
            print("\n>>> Coordinator Agent Selected\n")

        response = orchestrator.execute(user_input)

        print(response)


if __name__ == "__main__":
    main()