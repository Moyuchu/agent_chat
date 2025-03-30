import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm.base import DeepSeekService

def test_deepseek_call():
    llm_service = DeepSeekService()
    prompt = "Hello! Welcome to be my agent! "
    response = llm_service.call(prompt)
    assert response
    print(response)

if __name__ == '__main__':
    test_deepseek_call()
