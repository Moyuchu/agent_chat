from typing import Any, Optional
from src.tools.tool_interface import Tool
from src.config.settings import AGENT_SETTINGS

class ChatTool(Tool):
    def name(self) -> str:
        return "chat"

    def description(self) -> str:
        return """Continue chatting with the user
input:
- response: str, your reply content
output:
- None """
    def run(self, response: str, **kwargs) -> Any:
        print(f"\n{response}")
        return None
    def format_result(self, result: Any, params: dict) -> str:
        return ""
    
class AskGiftTool(Tool):
    def name(self) -> str:
        return "ask_gift"

    def description(self) -> str:
        return """Asks the user for a gift
input:
- response: str, your request for gift words
- gift_name: str, the desired gift name
output:
- gift_given: bool, whether the user agrees to send a gift"""

    def run(self, response: str, gift_name: str, **kwargs) -> Any:
        print(f"\n{AGENT_SETTINGS['name']}: {response}")
        print(f"\nwant gift is: {gift_name}")
        user_input = input("\nWould you like to send this gift? (y/n): ").lower()
        return user_input.startswith('y')
    def format_result(self, result: Any, params: dict) -> str:
        if result:
            return f"The user agrees to send you {params['gift_name']}!"
        return "The user declined the gift request"
    
class GiveGiftTool(Tool):
    def name(self) -> str:
        return "give_gift"

    def description(self) -> str:
        return """Gift to users
input:
- response: str, your gift words
- gift_name: str, the name of the gift to be sent
output:
- None"""

    def run(self, response: str, gift_name: str, **kwargs) -> Any:
        print(f"\n{AGENT_SETTINGS['name']}: {response}")
        print(f"\nGifts to you: {gift_name}")
        return None
    def format_result(self, result: Any, params: dict) -> str:
        return ""
    
class AskCoinsTool(Tool):
    def name(self) -> str:
        return "ask_coins"

    def description(self) -> str:
        return """Ask the user for coins
input:
- response: str, your request for game coin words
- amount: int, the number of coins you want
output:
- coins: int, the number of coins given by the user"""

    def run(self, response: str, amount: int, **kwargs) -> Any:
        print(f"\n{AGENT_SETTINGS['name']}: {response}")
        print(f"You want {amount} coins")
        user_input = input("\nPlease enter the number of coins to be given: ")
        return int(user_input)
    def format_result(self, result: Any, params: dict) -> str:
        return f"The user gave you {result} coins"
    
class IntimateActionTool(Tool):
    def name(self) -> str:
        return "intimate_action"

    def description(self) -> str:
        return """Perform intimate actions to the user
input:
- response: str, your words
- action: str, indicates the intimate action to be performed
output:
- None"""

    def run(self, response: str, action: str, **kwargs) -> Any:
        print(f"\n{AGENT_SETTINGS['name']}: {response}")
        print(f"执行动作: {action}")
        return None
    def format_result(self, result: Any, params: dict) -> str:
        return ""
    
class AngryEndTool(Tool):
    def name(self) -> str:
        return "angry_end"

    def description(self) -> str:
        return """End the conversation angrily

input:
- response: str, your reply content
output:
- None"""

    def run(self, response: str, **kwargs) -> Any:
        print(f"\n{AGENT_SETTINGS['name']}: {response}")
        print("\n[Session result]")
        return None
    
    def format_result(self, result: Any, params: dict) -> str:
        return ""
