import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent.base import Agent

async def test_rag():
    agent = Agent()
    print("Creating agent instance...")
    await agent.process_input(" Hello, I'd like to talk about my life lately." )
    print("Processed first input.")
    await agent.process_input(" I've been a little upset lately, can you help me?" )
    print("Processed second input.")
    await agent.process_input(" I was wondering if you've ever been in a similar situation before?" )
    print("Processed third input.")
    # 检查是否能检索
if __name__ == "__main__":
    print("Starting test...")
    asyncio.run(test_rag())
    print("Test completed.")