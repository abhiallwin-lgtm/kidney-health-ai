# utils/predict.py
import numpy as np
from joblib import load
import os

# Load model
model_path = os.path.join("model", "predictor.pkl")
model = load(model_path)

# Default values for all required features
FEATURES = ['blood_urea', 'creatinine', 'hemoglobin', 'sodium', 'potassium']

def predict_ckd(input_dict):
    # Convert input to ordered list
    input_values = [input_dict.get(f, np.nan) for f in FEATURES]

    # If any value is missing (NaN), return warning
    if any(np.isnan(input_values)):
        return "Incomplete Report", 0.0

    # Reshape for prediction
    X_input = np.array(input_values).reshape(1, -1)

    # Predict
    prediction = model.predict(X_input)[0]
    confidence = np.max(model.predict_proba(X_input)) * 100

    return prediction, confidence
