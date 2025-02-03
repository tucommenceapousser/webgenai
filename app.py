from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import base64
from io import BytesIO
from PIL import Image
import cv2
import numpy as np
import os
from dotenv import load_dotenv
from watermark import add_watermark

# Charger la clé API
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Config OpenAI
openai.api_key = OPENAI_API_KEY

app = FastAPI()

# Modèle de requête
class ImageRequest(BaseModel):
    prompt: str
    watermark: bool = True  # Activation du filigrane par défaut

@app.post("/generate-image/")
async def generate_image(request: ImageRequest):
    try:
        response = openai.Image.create(
            prompt=request.prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json"
        )
        
        # Récupérer l’image générée
        image_data = response['data'][0]['b64_json']
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))

        # Ajouter le filigrane si demandé
        if request.watermark:
            image = add_watermark(image, "trhacknon")

        # Convertir en base64 pour l’envoi
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return {"image": img_str}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
