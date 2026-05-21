import io
from functools import lru_cache

from fastapi import APIRouter, File, HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError
from transformers import pipeline

router = APIRouter(prefix="/image", tags=["image"])

MODEL_NAME = "Falconsai/nsfw_image_detection"


@lru_cache(maxsize=1)
def get_classifier():
    """Load the image-classification pipeline once and reuse it across requests."""
    return pipeline("image-classification", model=MODEL_NAME)


@router.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    """Classify an uploaded image with the NSFW detection model."""
    contents = await file.read()

    try:
        img = Image.open(io.BytesIO(contents)).convert("RGB")
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid image.")

    predictions = get_classifier()(img)

    return {
        "filename": file.filename,
        "predictions": predictions,
    }
