# api/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Bati Bank Credit Scoring API",
    description="API for credit risk prediction and loan optimization",
    version="1.0.0"
)

# Load models
try:
    lr_model = joblib.load('../credit_scoring_lr.pkl')
    rf_model = joblib.load('../credit_scoring_rf.pkl')
    logger.info("Models loaded successfully")
except Exception as e:
    logger.error(f"Error loading models: {str(e)}")
    raise RuntimeError("Failed to initialize API - models not loaded")

class CustomerData(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float
    TransactionHour: int
    TransactionDay: int
    TransactionMonth: int
    CurrencyCode: str
    CountryCode: str
    ProductId: str
    # Add other features from your dataset

class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    model_version: str
    timestamp: str

@app.get("/")
async def root():
    return {
        "message": "Bati Bank Credit Scoring API",
        "status": "healthy",
        "model_versions": {
            "logistic_regression": "1.0",
            "random_forest": "1.0"
        }
    }

@app.post("/predict/lr", response_model=PredictionResponse)
async def predict_lr(data: CustomerData):
    """Predict credit risk using Logistic Regression model"""
    return make_prediction(data, lr_model, "logistic_regression_1.0")

@app.post("/predict/rf", response_model=PredictionResponse)
async def predict_rf(data: CustomerData):
    """Predict credit risk using Random Forest model"""
    return make_prediction(data, rf_model, "random_forest_1.0")

def make_prediction(data: CustomerData, model, model_name: str):
    try:
        # Convert input data to DataFrame
        input_df = pd.DataFrame([data.dict()])
        
        # Preprocess and predict
        probability = model.predict_proba(input_df)[0][1]
        prediction = int(probability >= 0.5)  # Default threshold
        
        return {
            "prediction": prediction,
            "probability": round(probability, 4),
            "model_version": model_name,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)