import json
from typing import List
from src.agent.action import Action
from src.agent.memory import MemoryItem
from src.prompts.response import RESPONSE_PROMPT
from src.prompts.cot import CHAIN_OF_THOUGHT, PLAN_FORMAT
from src.tools.registry import ToolRegistry
# rag
# from rag.retrieval import KnowledgeRetriever 

def build_plan_prompt(user_message: str, history: List[MemoryItem]) -> str:
    history_lines = []
    for item in history:
        if item.role == "user":
            history_lines.append(f"Girlfriend: {item.message}")
        elif item.role == "assistant":
            history_lines.append(f"You: {item.message}")
        elif item.role == "action_result":
            history_lines.append(f"Girlfriend: {item.message}")
    history_text = "\n".join(history_lines) if history_lines else "No historical conversation is recorded"

    return CHAIN_OF_THOUGHT.format(
        history=history_text,
        user_message=user_message,
        plan_format=PLAN_FORMAT
    )

def build_response_prompt(
    user_message: str,
    plan: str,
    actions: List[Action],
    history: List[MemoryItem],
    # rag
    relevant_history: List[str] = []
) -> str:
    # rag
    print(f"Relevant history retrieved: {relevant_history}")  # 添加日志输出
    # rag
    # retriever = KnowledgeRetriever()  
    # retrieved_info = retriever.query(user_message)  # 查询外部知识

    # rag
    # response = f"Retrieval result: {retrieved_info}\n\n"
    # response += "Honey, let me tell you what I found: " + retrieved_info

    plan_lines = []
    for line in plan.strip().split('\n'):
        if not line.strip().startswith('#') or line.strip().startswith('##'):
            plan_lines.append(line)
    plan = '\n'.join(plan_lines).strip()

    history_lines = []
    for item in history:
        if item.role == "user":
            history_lines.append(f"Girlfriend: {item.message}")
        elif item.role == "assistant":
            history_lines.append(f"You: {item.message}")
        elif item.role == "action_result":
            history_lines.append(f"Girlfriend: {item.message}")
    history_text = "\n".join(history_lines) if history_lines else "No historical conversation is recorded"

    actions_text = "No action has been executed"
    if actions:
        registry = ToolRegistry()
        action_lines = []
        for action in actions:
            # 获取对应的工具
            tool = registry.get_tool(action.name)
            if tool:
                # 格式化参数和结果
                params = tool.format_params(action.params)
                result_text = tool.format_result(action.result, action.params)

                # 构建动作描述
                action_desc = f"- {action.name}"
                if params:
                    action_desc += f": {json.dumps(params, ensure_ascii=False)}"
                if result_text:
                    action_desc += f"\n  Result: {result_text}"

                action_lines.append(action_desc)

        actions_text = "\n".join(action_lines)
    # rag
    relevant_history_text = "\n".join(relevant_history) if relevant_history else "No related history"

    return RESPONSE_PROMPT.format(
        user_message=user_message,
        history=history_text,
        plan=plan,
        actions_text=actions_text,
        # rag
        relevant_history="\n".join(relevant_history) if relevant_history else "No related history"  # 添加检索结果
    )