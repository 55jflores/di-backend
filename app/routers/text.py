from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/text", tags=["text"])


class TextRequest(BaseModel):
    text: str


@router.post("/classify")
async def classify_text(payload: TextRequest):
    """Classify a piece of text.

    Skeleton only — classification logic to be filled in.
    """
    # TODO: run text classification on `payload.text` and return real results.
    return {
        "text": payload.text,
        "predictions": [],
    }
