FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app \
    HF_HOME=/opt/hf-cache

WORKDIR /app

# Install dependencies first so this layer is cached unless requirements change.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bake the model weights into the image. This layer is cached unless the
# download script or the code it imports changes, so rebuilds skip the download.
COPY app ./app
COPY scripts ./scripts
RUN python -m scripts.download_models

# Railway provides $PORT at runtime; default to 8000 for local `docker run`.
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
