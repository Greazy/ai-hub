from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query

from openai import OpenAI
from sqlalchemy.orm import Session

from models import Base, User
from database import engine, SessionLocal
from schemas import UserCreate

open_router_token=""

Base.metadata.create_all(bind=engine)

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=open_router_token,
    )

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(message: str = Query(..., description="Message from UI")):

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1",
        messages=[{"role": "user", "content": message}],
    )
    print('test')
    print(response.choices[0].message.content)
    return {"message": response.choices[0].message.content}

@app.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "email": new_user.email}