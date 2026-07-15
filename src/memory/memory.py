class MemoryManager:
    """
    Simple in-memory conversation store.

    Milestone 1:
    - Demonstrates short-term memory.
    - Can be replaced with Redis, ChromaDB,
      Pinecone or any Vector Database later.
    """

    def __init__(self):
        self.history = []

    def add(self, user, response):
        self.history.append(
            {
                "user": user,
                "assistant": response
            }
        )

    def get_history(self):
        return self.history

    def clear(self):
        self.history.clear()