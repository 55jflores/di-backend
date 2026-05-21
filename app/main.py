from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import base, image, text

app = FastAPI(
    title="di-backend",
    description="Image and text classification API.",
    version="0.1.0",
)

# Open CORS for now; tighten allow_origins before production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base.router)
app.include_router(image.router)
app.include_router(text.router)
