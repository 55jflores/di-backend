# di-backend

FastAPI backend for image and text classification, deployable on Railway.

## Routes

| Method | Path              | Description                          |
|--------|-------------------|--------------------------------------|
| GET    | `/`               | Health check — confirms the API is up |
| POST   | `/image/classify` | Upload an image to classify (`multipart/form-data`, field `file`) |
| POST   | `/text/classify`  | Send text to classify (`application/json`, `{"text": "..."}`) |

Interactive API docs are served at `/docs`.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://localhost:8000/docs

### Try the routes

```bash
# Base
curl http://localhost:8000/

# Image
curl -F "file=@path/to/image.jpg" http://localhost:8000/image/classify

# Text
curl -X POST http://localhost:8000/text/classify \
  -H "Content-Type: application/json" \
  -d '{"text": "some text to classify"}'
```

## Deploy to Railway

1. Push this repo to GitHub.
2. In Railway: **New Project → Deploy from GitHub repo**, select this repo.
3. Railway auto-detects Python (Nixpacks), installs `requirements.txt`, and runs the
   start command from `railway.json` (binds to Railway's `$PORT`).
4. Generate a public domain under the service's **Settings → Networking**.

No extra environment variables are required for the skeleton.

## Project layout

```
app/
  main.py            # FastAPI app + router registration
  routers/
    base.py          # GET /
    image.py         # POST /image/classify  (fill in classification logic)
    text.py          # POST /text/classify   (fill in classification logic)
requirements.txt
railway.json         # Railway build/deploy config
Procfile             # Fallback start command
runtime.txt          # Pins Python version
```

## Where to fill in logic

- **Image classification:** `app/routers/image.py` — see the `TODO` in `classify_image`.
- **Text classification:** `app/routers/text.py` — see the `TODO` in `classify_text`.
