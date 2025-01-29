from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the trained models
lr_model = joblib.load('credit_scoring_lr.pkl')
rf_model = joblib.load('credit_scoring_rf.pkl')

# Preprocessor (for consistency with the training pipeline)
numeric_features = ['Recency', 'Frequency', 'Monetary', 'TransactionCount', 'TransactionAmount', 'Stability', 'Value']
categorical_features = ['PricingStrategy', 'Region', 'PaymentType', 'DeviceType']

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Create FastAPI instance
app = FastAPI()

# Define input data model
class TransactionData(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float
    TransactionCount: int
    TransactionAmount: float
    Stability: float
    Value: float
    PricingStrategy: str
    Region: str
    PaymentType: str
    DeviceType: str

# Define prediction function
def predict(input_data: TransactionData, model):
    # Convert input data to DataFrame for preprocessing
    data_dict = input_data.dict()
    df = pd.DataFrame([data_dict])
    
    # Preprocess data
    processed_data = preprocessor.transform(df)
    
    # Make prediction
    prediction = model.predict(processed_data)
    return prediction[0]

@app.post("/predict_lr/")
async def predict_lr(input_data: TransactionData):
    prediction = predict(input_data, lr_model)
    return {"prediction": int(prediction)}

@app.post("/predict_rf/")
async def predict_rf(input_data: TransactionData):
    prediction = predict(input_data, rf_model)
    return {"prediction": int(prediction)}

