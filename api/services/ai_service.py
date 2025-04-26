import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_TOKEN"),
)

class AIService:
    def chat(self, message: str) -> str:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1",
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content