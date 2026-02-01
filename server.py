from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from datetime import datetime

# ----------------- APP -----------------
app = FastAPI(title="Clinical Decision Server")

# ----------------- LOAD MODELS -----------------
rf = joblib.load("rf_model.pkl")
xgb = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")

# ----------------- IN-MEMORY ALERT STORE -----------------
LATEST_VITALS_ALERTS = {}

# ----------------- PATIENT BASELINES -----------------
PATIENT_BASELINES = {
    "P001": {
        "type": "adult_hypertensive",
        "heart_rate": (70, 95),
        "spo2": (94, 100),
        "systolic": (130, 160),
        "diastolic": (80, 100),
        "temperature": (36.5, 37.5)
    },
    "P002": {
        "type": "adult_normal",
        "heart_rate": (60, 90),
        "spo2": (95, 100),
        "systolic": (110, 130),
        "diastolic": (70, 85),
        "temperature": (36.5, 37.5)
    },
    "C001": {
        "type": "child",
        "heart_rate": (90, 120),
        "spo2": (95, 100),
        "systolic": (90, 110),
        "diastolic": (55, 75),
        "temperature": (36.5, 37.8)
    }
}

# ----------------- INPUT SCHEMA -----------------
class VitalsJSON(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    temperature: float
    systolic: int
    diastolic: int

# ----------------- RULE CHECK -----------------
def check_deviation(v, base):
    deviations = []

    if not (base["heart_rate"][0] <= v.heart_rate <= base["heart_rate"][1]):
        deviations.append("Heart Rate")

    if not (base["spo2"][0] <= v.spo2 <= base["spo2"][1]):
        deviations.append("SpO₂")

    if not (base["systolic"][0] <= v.systolic <= base["systolic"][1]):
        deviations.append("Systolic BP")

    if not (base["diastolic"][0] <= v.diastolic <= base["diastolic"][1]):
        deviations.append("Diastolic BP")

    if not (base["temperature"][0] <= v.temperature <= base["temperature"][1]):
        deviations.append("Temperature")

    return deviations

# ----------------- ANALYZE ENDPOINT -----------------
@app.post("/analyze")
def analyze_vitals(v: VitalsJSON):

    baseline = PATIENT_BASELINES.get(v.patient_id)
    if baseline is None:
        return {"error": "Unknown patient", "alert": True}

    deviations = check_deviation(v, baseline)

    input_df = pd.DataFrame([{
        "Heart Rate": v.heart_rate,
        "Respiratory Rate": 18,
        "Body Temperature": v.temperature,
        "Oxygen Saturation": v.spo2,
        "Systolic Blood Pressure": v.systolic,
        "Diastolic Blood Pressure": v.diastolic,
        "Age": 45,
        "Gender": 0,
        "Weight (kg)": 65,
        "Height (m)": 1.65,
        "Derived_HRV": 0,
        "Derived_Pulse_Pressure": v.systolic - v.diastolic,
        "Derived_BMI": 65 / (1.65 ** 2),
        "Derived_MAP": (v.systolic + 2 * v.diastolic) / 3
    }])

    X = scaler.transform(input_df)

    rf_prob = rf.predict_proba(X)[0][1]
    xgb_prob = xgb.predict_proba(X)[0][1]
    ml_risk = round((rf_prob + xgb_prob) / 2, 2)

    alert = bool(deviations) or ml_risk > 0.6

    # 🔔 STORE ALERT FOR DASHBOARD
    LATEST_VITALS_ALERTS[v.patient_id] = {
        "module": "vitals",
        "patient_id": v.patient_id,
        "patient_type": baseline["type"],
        "ml_risk_score": ml_risk,
        "deviations": deviations,
        "alert": alert,
        "timestamp": datetime.now().isoformat()
    }

    return LATEST_VITALS_ALERTS[v.patient_id]

# ----------------- DASHBOARD ENDPOINT -----------------
@app.get("/dashboard/alerts")
def get_dashboard_alerts():
    return list(LATEST_VITALS_ALERTS.values())
