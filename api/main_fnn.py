from numpy import array, expand_dims
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from tensorflow.keras.models import load_model


class InferenceRequest(BaseModel):
    features: List[int]


app = FastAPI(
    title="TensorFlow Model API",
    description="Eine performante API für Modell-Inference mit FastAPI",
    version="1.0"
)

try:
    model = load_model("model_fnn.keras")
    print("Modell erfolgreich geladen!")
except Exception as e:
    print(f"Fehler beim Laden des Modells: {e}")
    model = None

@app.post("/predict")
async def predict(payload: InferenceRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Modell ist nicht verfügbar")

    try:
        input_data = array(payload.features)

        if input_data.ndim == 1:
            input_data = expand_dims(input_data, axis=0)

        predictions = model.predict(input_data)
        output = predictions.tolist()
        return {"prediction": output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"status": "online", "model_loaded": model is not None}
