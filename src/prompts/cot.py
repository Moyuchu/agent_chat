from src.prompts.identity import IDENTITY

PLAN_FORMAT = """ 
1. User's intent analysis: [Analyze user's intent and emotional state]
2. Historical relations: [Analyze the historical relationship between the user and agent, if any]
3. Action plan: [Detailed description of how the agent will respond, including possible actions]
"""

CHAIN_OF_THOUGHT = f"""{IDENTITY}

# Dialogue Information
## Historical dialogue record
{{history}}

## Current Dialogue
user said: {{user_message}}

# Thought Process
1. Understand the user's current emotional state and needs
2. Review the history of interactions between us
3. Decide the most suitable response

# Action Plan
{{plan_format}}

Please make action plan according to the above information for the reference of subsequent response. Remember to keep your man set.
"""
