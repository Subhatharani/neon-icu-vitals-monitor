# profiles.py

PATIENT_PROFILES = {

    # -------------------------
    # NORMAL ADULT
    # -------------------------
    "adult_normal": {
        "heart_rate": {"base": 72, "min": 60, "max": 100, "step": 2},
        "spo2": {"base": 98, "min": 95, "max": 100, "step": 0.5},
        "temperature": {"base": 36.8, "min": 36.2, "max": 37.5, "step": 0.05},
        "systolic": {"base": 120, "min": 110, "max": 130, "step": 2},
        "diastolic": {"base": 80, "min": 70, "max": 85, "step": 1.5}
    },

    # -------------------------
    # HYPERTENSIVE PATIENT
    # -------------------------
    "adult_hypertensive": {
        "heart_rate": {"base": 85, "min": 70, "max": 110, "step": 3},
        "spo2": {"base": 96, "min": 92, "max": 100, "step": 0.7},
        "temperature": {"base": 37.0, "min": 36.5, "max": 38.0, "step": 0.06},
        "systolic": {"base": 150, "min": 135, "max": 180, "step": 3},
        "diastolic": {"base": 95, "min": 85, "max": 110, "step": 2}
    },

    # -------------------------
    # HYPOTENSIVE PATIENT
    # -------------------------
    "adult_hypotensive": {
        "heart_rate": {"base": 95, "min": 80, "max": 130, "step": 3},
        "spo2": {"base": 94, "min": 88, "max": 98, "step": 0.8},
        "temperature": {"base": 36.5, "min": 35.8, "max": 37.2, "step": 0.06},
        "systolic": {"base": 90, "min": 75, "max": 100, "step": 2},
        "diastolic": {"base": 60, "min": 45, "max": 65, "step": 1.5}
    },

    # -------------------------
    # CHILD
    # -------------------------
    "child": {
        "heart_rate": {"base": 105, "min": 90, "max": 130, "step": 3},
        "spo2": {"base": 98, "min": 95, "max": 100, "step": 0.6},
        "temperature": {"base": 37.0, "min": 36.5, "max": 37.8, "step": 0.05},
        "systolic": {"base": 100, "min": 90, "max": 115, "step": 2},
        "diastolic": {"base": 65, "min": 55, "max": 75, "step": 1.2}
    }
}
