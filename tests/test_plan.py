import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from src.agent.plan import Planner
from src.agent.memory import MemoryItem

def test_create_plan():
    planner = Planner()
    history = [
        MemoryItem(
            user_input="Hi Caleb!",
            ai_response="Hello, nice to meet you!",
            timestamp=datetime.now(),
            actions=[]
        ),
        MemoryItem(
            user_input="How's the weather today?",
            ai_response="It's sunny, should we go out?",
            timestamp=datetime.now(),
            actions=[]
        )
    ]

    user_message = "I don't feel very good today"
    plan = planner.create_plan(user_message, history)
    assert plan
    print(plan)

if __name__ == '__main__':
    test_create_plan()
