# simulator.py

import time
import random
import json
from profiles import PATIENT_PROFILES
import requests

SERVER_URL = "http://127.0.0.1:8000/analyze"

# ================================
# SELECT PATIENT TYPE HERE
# ================================
PATIENT_ID = "P003"
PATIENT_TYPE = "adult_hypotensive"  
# options:
# adult_normal
# adult_hypertensive
# adult_hypotensive
# child

profile = PATIENT_PROFILES[PATIENT_TYPE]

# ================================
# INITIALIZE PATIENT STATE
# ================================
def initialize_state(profile):
    return {
        vital: profile[vital]["base"]
        for vital in profile
    }

state = initialize_state(profile)

# ================================
# UPDATE LOGIC (PHYSIOLOGICAL)
# ================================
def update_vital(value, min_v, max_v, step):
    value += random.uniform(-step, step)
    return round(max(min_v, min(max_v, value)), 2)

def update_state(state, profile):
    for vital, config in profile.items():
        state[vital] = update_vital(
            state[vital],
            config["min"],
            config["max"],
            config["step"]
        )
    return state

# ================================
# RARE CLINICAL EVENTS
# ================================
def maybe_emergency(state):
    if random.random() < 0.03:
        print("⚠️  Emergency event simulated")
        state["spo2"] -= random.randint(3, 7)
        state["heart_rate"] += random.randint(10, 25)
        state["systolic"] -= random.randint(5, 15)
    return state

# ================================
# CONTINUOUS STREAM
# ================================
print(f"📡 Starting simulation for {PATIENT_TYPE} ({PATIENT_ID})\n")

while True:
    state = update_state(state, profile)
    state = maybe_emergency(state)

    payload = {
    "patient_id": PATIENT_ID,
    "heart_rate": int(state["heart_rate"]),
    "spo2": int(state["spo2"]),
    "temperature": float(state["temperature"]),
    "systolic": int(state["systolic"]),
    "diastolic": int(state["diastolic"])
}

    try:
        requests.post(SERVER_URL, json=payload, timeout=2)
        print("📤 Sent:", payload)
    except Exception as e:
        print("❌ Failed to send:", e)

    time.sleep(2)
