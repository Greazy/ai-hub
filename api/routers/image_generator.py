from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import os
from io import BytesIO


router = APIRouter()

STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

class ImageRequest(BaseModel):
    prompt: str

@router.post("/generate-image")
def generate_image(request: ImageRequest):
    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": f"Bearer {STABILITY_API_KEY}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": request.prompt,
            "output_format": "jpeg",
        },
    )

    if response.status_code == 200:
        with open("./lighthouse.jpeg", 'wb') as file:
            file.write(response.content)

        image_stream = BytesIO(response.content)
        return StreamingResponse(image_stream, media_type="image/jpeg")
    else:
        try:
            error_info = response.json()
        except Exception:
            error_info = {"detail": "Unknown error"}
        raise HTTPException(status_code=response.status_code, detail=error_info)
    
    
