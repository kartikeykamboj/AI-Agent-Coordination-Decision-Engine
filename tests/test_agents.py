import os
import sys

# Add the src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from agents.coordinator import CoordinatorAgent


def test_coordinator_creation():
    agent = CoordinatorAgent()
    assert agent is not None