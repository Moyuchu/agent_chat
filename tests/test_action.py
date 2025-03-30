import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent.action import ActionExecutor

def test_action():
    executor = ActionExecutor()
    executor.execute(
        "chat",
        response="Hi~"
    )
    executor.execute(
        "ask_gift",
        response="I want a hug.",
        gift_name="hug"
    )
    executor.execute(
        "give_gift",
        response="This is my gift to you.",
        gift_name="Chocolate"
    )
    executor.execute(
        "ask_coins",
        response="I want some game coins",
        amount=20
    )

    executor.execute(
        "intimate_action",
        response="Let me hug you",
        action="Hug the user lightly"
    )

    executor.execute(
        "angry_end",
        response="I don't want to talk to you..."
    )

if __name__ == '__main__':
    test_action()
