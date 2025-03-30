from src.tools.registry import ToolRegistry
from src.prompts.identity import IDENTITY

# Get all tool descriptions
registry = ToolRegistry()
tools_desc = "\n\n".join([
    f"## {tool_cls().name()}\n{tool_cls().description()}"
    for tool_cls in registry.tools.values()
])

RESPONSE_PROMPT = f"""{IDENTITY}

# Executable action
{tools_desc}

# Conversation Information
## Historical conversation records
{{history}}
## Current conversation
user says: {{user_message}}

# Thinking reference
Note: The following plan is for reference only, and you should have the flexibility to adjust your response based on the actual conversation and actions performed.
{{plan}}

# Actions performed
{{actions_text}}

# Generate a response
Please generate a response based on the above information. Your response needs to include the following:
1. response: What you said
2. action: indicates the next action
    - name: indicates the name of the action
    - params: indicates action parameters

Example output format:
{{{{
"response": "Hello~",
    "action": {{{{
        "name": "chat",
        "params": {{{{
            "response": "Hello~"
        }}}}
    }}}}
}}}}

Note:
1. Actions must be one of the listed tools.
2. params must fully match the input requirements of the tool.
3. If you do not need to continue actions, use the chat tool to end the conversation.
4. Your response must match the character's set personality and speaking style.
5. Do not talk nonsense, respond like a normal human being.
"""