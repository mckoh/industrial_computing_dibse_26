import io
import numpy as np
from numpy import expand_dims, array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image


IMG_WIDTH = 224
IMG_HEIGHT = 224


app = FastAPI(title="TensorFlow Image Model API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    model = load_model("model_cnn.keras")
except Exception as e:
    model = None


@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):
    if model is None:
        raise HTTPException(status_code=500, detail="Modell ist nicht verfügbar")

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Datei ist kein gültiges Bild.")

    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        if image.mode != "RGB":
            image = image.convert("RGB")

        image = image.resize((IMG_WIDTH, IMG_HEIGHT))

        img_array = array(image) / 255.0
        img_array = expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        predictions = model.predict(img_array)
        output = predictions.tolist()

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "prediction": output
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fehler bei der Verarbeitung: {str(e)}")