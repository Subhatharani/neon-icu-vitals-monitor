import requests
import random
import time

URL = "http://127.0.0.1:8000/analyze"

print("📡 Simulator started")

while True:
    abnormal = random.choice([False, False, True])

    if abnormal:
        print("🚨 FORCING ABNORMAL VITALS")
        data = {
            "patient_id": "P001",
            "heart_rate": random.randint(130, 150),
            "spo2": random.randint(85, 90),
            "temperature": round(random.uniform(38.6, 39.5), 2),
            "systolic": random.randint(170, 190),
            "diastolic": random.randint(100, 120)
        }
    else:
        print("✅ Normal vitals")
        data = {
            "patient_id": "P001",
            "heart_rate": random.randint(70, 90),
            "spo2": random.randint(96, 99),
            "temperature": round(random.uniform(36.6, 37.2), 2),
            "systolic": random.randint(110, 130),
            "diastolic": random.randint(70, 85)
        }

    try:
        r = requests.post(URL, json=data)
        print("Sent | Alert:", r.json()["alert"])
    except:
        print("❌ Server not reachable")

    time.sleep(2)
