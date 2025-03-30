from typing import Any, List, Tuple, Dict
import json
from src.agent.plan import Planner
from src.agent.memory import Memory
from src.agent.action import Action, ActionExecutor
from src.llm.base import LLMService, DeepSeekService
from src.prompts.builder import build_response_prompt

class Agent:
    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.llm = DeepSeekService()
        self.executor = ActionExecutor()

    async def process_input(self, user_message: str) -> str:
        await self.memory.add_memory(user_message, role="user")

        # 检索相关历史会话 rag
        relevant_history = self.memory.retrieve_relevant(user_message, top_k=3)
        print(f"Retrieved relevant history: {relevant_history}")  # 添加日志输出
        
        plan: str = self.planner.create_plan(user_message, self.memory.memory)
        response: str = self._gen_response(user_message, plan)
        thought, data = self._parse_response(response)
        
        cur_actions: List[Action] = []
        while data != {}:
            action_name = data.get("name", "")
            params = data.get("params", {})

            action = self.executor.execute(action_name, **params)
            cur_actions.append(action)

            tool = self.executor.tool_registry.get_tool(action_name)
            if action_name in ["end", "angry_end", "chat"]:
                await self.memory.add_memory(thought, role="assistant")
                break

            await self.memory.add_memory(thought, role="assistant")
            result_text = tool.format_result(action.result, action.params)
            await self.memory.add_memory(result_text, role="action_result")
            
            response = self._gen_response(user_message, plan, cur_actions)
            thought, data = self._parse_response(response)

        return thought
    
    def _gen_response(self, user_message: str, plan: str, actions: List[Action] = [], relevant_history: List[str] = []) -> str:
        prompt = build_response_prompt(
            user_message=user_message,
            plan=plan,
            actions=actions,
            history=self.memory.memory,
            # rag
            relevant_history=relevant_history
        )
        print(prompt)
        print()
        return self.llm.call(prompt)

    def _parse_response(self, response: str) -> Tuple[str, Dict[str, Any]]:
        print(f"Raw response from LLM: {response}")  # 添加日志输出
        try:
            data = json.loads(response)
            thought = data.get("response", "")
            action_data = data.get("action", {})
            return thought, action_data
        except json.JSONDecoder:
            print(f"fail: {response}")
            return "", {}