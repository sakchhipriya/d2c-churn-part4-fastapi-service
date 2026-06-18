from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.pkl")


class CustomerData(BaseModel):
    recency: float
    frequency: float
    monetary: float
    ticket_count: float
    return_rate: float
    sessions_30d: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: CustomerData):

    df = pd.DataFrame([data.dict()])

    probability = float(
        model.predict_proba(df)[0][1]
    )

    prediction = int(
        model.predict(df)[0]
    )

    if probability >= 0.7:
        risk = "high"
    elif probability >= 0.4:
        risk = "medium"
    else:
        risk = "low"

    return {
        "churn_probability": round(probability, 2),
        "predicted_class": prediction,
        "risk_level": risk,
        "risk_explanation":
        "Low engagement and support issues may indicate churn risk."
    }

# Batch Predict Endpoint

class BatchRequest(BaseModel):
    customers: list[CustomerData]


@app.post("/batch_predict")
def batch_predict(request: BatchRequest):

    results = []

    for customer in request.customers:

        df = pd.DataFrame([customer.dict()])

        probability = float(
            model.predict_proba(df)[0][1]
        )

        prediction = int(
            model.predict(df)[0]
        )

        results.append({
            "churn_probability": round(probability,2),
            "predicted_class": prediction
        })

    return {"predictions": results}
