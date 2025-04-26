from fastapi import APIRouter
from schemas import ChatRequest
from services.ai_service import AIService

router = APIRouter()
ai = AIService()


@router.post("/chat")
def chat(req: ChatRequest):
    reply = ai.chat(req.message)
    return {"message": reply}


