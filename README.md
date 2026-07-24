# Vital Simulator and Outlier Detection for Real-Time Clinical Monitoring

**Author:** Subha Tharani

---

# Preface

Continuous monitoring of patient vital signs is critical in clinical environments such as ICUs, emergency wards, and remote healthcare systems. However, collecting real-time physiological data for testing and validation is often difficult due to privacy, hardware, and logistical constraints.

This project presents a **real-time vital signs simulation framework combined with outlier detection and clinical alerting logic**. The system simulates realistic patient vitals, adapts to patient-specific baselines, detects abnormal deviations, and generates alerts suitable for doctor-facing dashboards.

The project is designed for **healthcare system prototyping, hackathons, academic demonstrations, and AI/ML research**.

---

# Features

- Real-time patient vital simulation
- Multiple patient profiles
- Personalized baseline modeling
- Rule-based anomaly detection
- Machine learning risk prediction
- Live dashboard visualization
- Clinical alert generation
- REST API-based communication

---

# Table of Contents

1. Problem Definition
2. System Architecture
3. Vital Simulation Module
4. Patient Baseline Modeling
5. Outlier Detection Logic
6. Alert Generation
7. Dashboard Integration
8. Experimental Validation
9. Applications
10. Repository Structure
11. Installation
12. Future Enhancements
13. Contributors

---

# Problem Definition

The objective of this project is to continuously simulate patient vital signs and detect abnormalities relative to each patient's physiological baseline.

Instead of relying solely on universal threshold values, the system evaluates each patient's vitals against their personalized baseline, resulting in more realistic clinical monitoring.

---

# System Architecture

The project follows a modular architecture consisting of:

- Vital Simulator
- Baseline Generator
- Outlier Detection Engine
- Machine Learning Risk Predictor
- Backend Server
- Real-Time Dashboard

Each module operates independently and communicates through lightweight APIs.

---

# Vital Simulation Module

The simulator generates realistic physiological values every 1–2 seconds.

## Simulated Parameters

- Heart Rate (BPM)
- Oxygen Saturation (SpO₂)
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Body Temperature

## Supported Patient Profiles

- Normal Adult
- Hypertensive Adult
- Hypotensive Adult
- Child

The simulator can also generate controlled abnormal events for testing and demonstrations.

---

# Patient Baseline Modeling

Each patient has a personalized baseline determined by:

- Age
- Patient category
- Medical condition

Incoming vitals are evaluated against these individualized baselines instead of fixed clinical thresholds.

---

# Outlier Detection Logic

The project combines two approaches.

### Rule-Based Detection

Checks whether any vital exceeds its permitted baseline range.

### Machine Learning Risk Prediction

Risk is estimated using:

- Random Forest
- XGBoost

A patient is considered abnormal when:

- One or more vitals exceed their baseline
- OR
- The predicted ML risk score exceeds the configured threshold.

---

# Alert Generation

Whenever abnormal conditions are detected, the backend generates alerts containing:

- Patient ID
- Patient Profile
- Deviating Vital Signs
- Risk Score
- Timestamp

These alerts are immediately available to the dashboard.

---

# Dashboard Integration

The dashboard provides:

- Live vital monitoring
- Dynamic line graphs
- Patient status
- Alert history
- Doctor-friendly notifications

---

# Experimental Validation

The system was tested using:

- Continuous real-time simulation
- Multiple patient profiles
- Artificial abnormal events
- Dashboard alert verification

Results demonstrated successful alert generation within seconds of detecting abnormal conditions.

---

# Applications

- ICU Monitoring
- Remote Patient Monitoring
- Healthcare IoT
- Medical AI Research
- Clinical Decision Support
- Academic Projects
- Hackathons

---

# Repository Structure

```text
neon-icu-vitals-monitor/
│
├── backend/
├── frontend/
├── models/
├── simulator/
├── dataset/
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Subhatharani/neon-icu-vitals-monitor.git
```

Move into the project directory:

```bash
cd neon-icu-vitals-monitor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend and dashboard according to the project setup.

---

# Future Enhancements

- Wearable sensor integration
- LSTM-based anomaly detection
- Doctor mobile notifications
- Multi-patient dashboard
- Electronic Health Record (EHR) integration
- Cloud deployment

---

# Contributors

- **Subha Tharani** — Project Author
- **Vigneshwar Balakumar** — Documentation & Repository Contribution

---

# License

This project is intended for academic, research, and demonstration purposes.

---

## Acknowledgements

Special thanks to all contributors and mentors who supported the development, testing, and documentation of this healthcare monitoring project.