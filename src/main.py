import sys
import os
import asyncio

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from src.agent.base import Agent

async def main():
    agent = Agent()
    print("Your boyfriend is online, start chatting!")

    while True:
        try:
            user_input = input("\nYou:").strip()

            if user_input.lower() in ['exit', 'quit', '退出']:
                print("\nGoodbye! Looking forward to seeing you next time!")
                break

            if not user_input:
                continue

            response = await agent.process_input(user_input)

        except KeyboardInterrupt:
            print("\n\nGoodbye! Looking forward to seeing you next time!")
            break

        except Exception as e:
            import traceback
            print(f"\nSorry, there's a slight problem: {str(e)}")
            traceback.print_exc()  # 这会打印完整的错误堆栈
            continue

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nGoodbye! Looking forward to seeing you next time!")
        sys.exit(0)