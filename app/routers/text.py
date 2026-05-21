from functools import lru_cache

from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter(prefix="/text", tags=["text"])

MODEL_NAME = "michellejieli/NSFW_text_classifier"


class TextRequest(BaseModel):
    text: str


@lru_cache(maxsize=1)
def get_classifier():
    """Load the sentiment-analysis pipeline once and reuse it across requests."""
    return pipeline("sentiment-analysis", model=MODEL_NAME)


@router.post("/classify")
async def classify_text(payload: TextRequest):
    """Classify a piece of text with the NSFW text classification model."""
    predictions = get_classifier()(payload.text)

    return {
        "text": payload.text,
        "predictions": predictions,
    }
