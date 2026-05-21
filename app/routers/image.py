from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix="/image", tags=["image"])


@router.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    """Classify an uploaded image.

    Skeleton only — classification logic to be filled in.
    """
    contents = await file.read()

    # TODO: run image classification on `contents` and return real results.
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(contents),
        "predictions": [],
    }
