from typing import Any, Dict
from dataclasses import dataclass
from src.tools.registry import ToolRegistry

_FUNCTION = Any

@dataclass
class Action:
    name: str
    params: Dict[str, Any]
    result: Any = None

class ActionExecutor:
    def __init__(self):
        self.tool_registry = ToolRegistry()

    def execute(self, action_name: str, **kwargs) -> Action:
        try:
            tool = self.tool_registry.get_tool(action_name)
            result = tool.run(**kwargs)
            return Action(
                name=action_name,
                params=kwargs,
                result=result
            )
        except Exception as e:
            print(f"An error occurred while executing action {action_name}: {str(e)}")
            return Action(
                name=action_name,
                params=kwargs,
                result={"status": "error", "message": str(e)}
            )