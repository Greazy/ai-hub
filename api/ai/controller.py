import subprocess
from ai.parser import AIParser
from ai.executor import AIExecutor
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AICommandController:
    def __init__(self):
        self.parser = AIParser()
        self.executor = AIExecutor()

    async def handle(self, message: str):
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1",
            messages=[{"role": "user", "content": message}],
        )

        ai_response = response.choices[0].message.content
        print(f"AI Response: {ai_response}")
        
        commands = self.parser.parse(ai_response)
        results = []

        for command in commands:
            result = self.executor.execute(command)
            results.append(result)

        return results