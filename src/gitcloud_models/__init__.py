from fastapi import APIRouter, HTTPException

models = APIRouter()

@models.post("/")
async def create_model():
    raise HTTPException(status_code=501, detail="Not Implemented")

@models.post("/{model_id}/train")
async def train_model():
    raise HTTPException(status_code=501, detail="Not Implemented")

@models.post("/{model_id}/predict")
async def predict_model():
    raise HTTPException(status_code=501, detail="Not Implemented")

@models.post("/{model_id}/validate")
async def validate_model():
    raise HTTPException(status_code=501, detail="Not Implemented")
