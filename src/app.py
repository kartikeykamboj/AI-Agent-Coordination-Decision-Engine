from workflow.orchestrator import WorkflowOrchestrator


def main():
    print("=" * 60)
    print(" AI Agent Coordination & Decision Engine ")
    print("=" * 60)
    print("Infosys Springboard Virtual Internship 7.0")
    print("Milestone 1 Prototype")
    print("=" * 60)

    orchestrator = WorkflowOrchestrator()

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nSession Ended.")
            break

        response = orchestrator.execute(user_input)

        print("\nCoordinator Agent:\n")
        print(response)


if __name__ == "__main__":
    main()