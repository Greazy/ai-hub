from fastapi import APIRouter
from pydantic import BaseModel
from ai.controller import AICommandController

router = APIRouter()

class AICommandRequest(BaseModel):
    message: str

@router.post("/ai-command")
async def ai_command(request: AICommandRequest):
    controller = AICommandController()
    result = await controller.handle(request.message)
    return {"status": "success", "details": result}