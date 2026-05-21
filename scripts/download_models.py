"""Pre-download model weights at build time so they ship inside the image.

Reuses the routers' loaders so the model names stay in one place. Running each
loader populates the Hugging Face cache (HF_HOME) baked into the Docker image.
"""

from app.routers import image, text


def main():
    print("Pre-downloading image-classification model...", flush=True)
    image.get_classifier()
    print("Pre-downloading text-classification model...", flush=True)
    text.get_classifier()
    print("Done. Model weights are cached in the image.", flush=True)


if __name__ == "__main__":
    main()
