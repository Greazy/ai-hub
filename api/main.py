from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query

# from openai import OpenAI

from dotenv import load_dotenv

from models import Base, User
from db import engine, get_db

from services.ai_service import AIService

from routers import chat, users, health, image_generator

load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(health.router, prefix="/health")
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(image_generator.router, prefix="/generate-image", tags=["GenerateImage"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPEN_ROUTER_TOKEN"),
# )

# @app.get("/")
# def read_root(message: str = Query(..., description="Message from UI")):

#     response = client.chat.completions.create(
#         model="deepseek/deepseek-r1",
#         messages=[{"role": "user", "content": message}],
#     )
#     print('test')
#     print(response.choices[0].message.content)
#     return {"message": response.choices[0].message.content}

