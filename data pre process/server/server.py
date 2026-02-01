from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------- JSON schema ----------
class VitalPacket(BaseModel):
    patient_id: str
    patient_type: str
    timestamp: float
    vitals: dict

# -------- Receive vitals ----------
@app.post("/vitals")
def receive_vitals(data: VitalPacket):
    print("📥 Received data:")
    print(data)
    return {"status": "received"}
