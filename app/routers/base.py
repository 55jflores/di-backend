from fastapi import APIRouter

router = APIRouter(tags=["base"])


@router.get("/")
def root():
    """Health check / landing route."""
    return {"status": "ok", "message": "di-backend is up and running."}
