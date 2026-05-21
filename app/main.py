from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import base, image, text


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Warm both pipelines at startup so the first request doesn't pay the
    # model-loading cost. Weights are baked into the image (see Dockerfile),
    # so this is just an in-memory load, not a download.
    image.get_classifier()
    text.get_classifier()
    yield


app = FastAPI(
    title="di-backend",
    description="Image and text classification API.",
    version="0.1.0",
    lifespan=lifespan,
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
