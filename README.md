# D2C Customer Churn Prediction API

## Project Overview

This project provides a FastAPI-based churn prediction service that loads a trained Random Forest model and exposes prediction endpoints for customer churn scoring.

The API is designed to support CRM and retention teams by identifying customers at risk of churn.

---

## Project Structure

```text
d2c-churn-part4-fastapi-service/

├── README.md
├── requirements.txt
├── model.pkl
├── monitoring_plan.md
├── test_api.py
│
└── app/
    └── main.py
```

---

## Model Information

* Model Type: Random Forest Classifier
* Source: Part 3 Churn Prediction Model
* Output:

  * Churn Probability
  * Predicted Class
  * Risk Level
  * Risk Explanation

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Available Endpoints

### GET /health

Health check endpoint.

Sample Response:

```json
{
  "status": "ok"
}
```

---

### POST /predict

Returns churn prediction for a single customer.

Sample Request:

```json
{
  "recency": 30,
  "frequency": 5,
  "monetary": 1000,
  "ticket_count": 1,
  "return_rate": 0.1,
  "sessions_30d": 10
}
```

Sample Response:

```json
{
  "churn_probability": 0.72,
  "predicted_class": 1,
  "risk_level": "high",
  "risk_explanation": "Low engagement and support issues may indicate churn risk."
}
```

---

### POST /batch_predict

Returns churn predictions for multiple customers.

Sample Request:

```json
{
  "customers": [
    {
      "recency": 30,
      "frequency": 5,
      "monetary": 1000,
      "ticket_count": 1,
      "return_rate": 0.1,
      "sessions_30d": 10
    }
  ]
}
```

---

## Running Tests

Execute API tests:

```bash
pytest test_api.py
```

---

## Reproducibility

Install all required dependencies using:

```bash
pip install -r requirements.txt
```

The repository includes the trained model artifact (`model.pkl`) required for inference.

---

## Monitoring

Monitoring requirements are documented in:

```text
monitoring_plan.md
```

Key monitoring areas include:

* Data Drift
* Prediction Distribution
* Business Outcomes
* API Errors
* Retraining Triggers

---

## Responsible Use

The API is intended to support retention and customer engagement decisions.

Predictions should not be used as the sole basis for automated actions, customer exclusion, or service denial without human review.
