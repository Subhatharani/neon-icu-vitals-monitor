from fastapi import FastAPI
from pydantic import BaseModel
from time import time

app = FastAPI(title="Vitals Server")

LATEST = []

class Vitals(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    temperature: float
    systolic: int
    diastolic: int

def is_abnormal(v):
    if v.heart_rate < 50 or v.heart_rate > 120:
        return True
    if v.spo2 < 92:
        return True
    if v.systolic > 160 or v.systolic < 90:
        return True
    if v.temperature > 38.5:
        return True
    return False

@app.post("/analyze")
def analyze(v: Vitals):
    alert = is_abnormal(v)

    record = {
        "patient_id": v.patient_id,
        "heart_rate": v.heart_rate,
        "spo2": v.spo2,
        "temperature": v.temperature,
        "systolic": v.systolic,
        "diastolic": v.diastolic,
        "alert": alert,
        "timestamp": time()
    }

    LATEST.append(record)
    if len(LATEST) > 30:
        LATEST.pop(0)

    return {"alert": alert}

@app.get("/dashboard")
def dashboard():
    return LATEST
