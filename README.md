Vital Simulator and Outlier Detection for Real-Time Clinical Monitoring
Author: Subha Tharani

## 0. Preface

Continuous monitoring of patient vital signs is critical in clinical environments such as ICUs, emergency wards, and remote healthcare systems. However, collecting real-time physiological data for testing and validation is often difficult due to privacy, hardware, and logistical constraints.

This project presents a **real-time vital signs simulation framework combined with outlier detection and clinical alerting logic**. The system simulates realistic patient vitals, adapts to patient-specific baselines, detects abnormal deviations, and generates alerts suitable for doctor-facing dashboards.

The project is designed for **healthcare system prototyping, hackathons, and academic demonstrations**.



## 0.1 Updates

- Real-time vitals simulation implemented
- Multiple patient profiles supported
- Personalized baseline modeling added
- Outlier detection logic integrated
- Server-dashboard communication established
- Alert generation verified in live demo



## 0.2 Table of Contents

Vital Simulator and Outlier Detection  
      0. Preface  
      0.1 Updates  
      0.2 Table of Contents   
      1. Problem Definition  
      2. System Architecture  
      3. Vital Simulation Module  
      4. Patient Baseline Modeling  
      5. Outlier Detection Logic  
      6. Alert Generation  
      7. Dashboard Integration  
      8. Experimental Validation  
      9. Applications  
      10. Limitations  
      11. Future Work  



1. Problem Definition

The goal of this project is to simulate continuous patient vital signs and detect abnormal patterns relative to each patient’s physiological baseline.

Given a stream of vitals \( V_t \) at time \( t \), the system determines whether the current state is:
- Normal
- Deviating
- Clinically abnormal (alert-worthy)

This approach mirrors real clinical monitoring, where abnormality is **personalized**, not based on a single global threshold.



## 2. System Architecture

The system follows a modular real-time pipeline:


Each component runs independently and communicates via lightweight HTTP APIs.


## 3. Vital Simulation Module

The simulation module generates realistic vitals at a fixed frequency (1–2 seconds per update).

### Simulated Vitals
- Heart Rate (bpm)
- Oxygen Saturation (SpO₂ %)
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Body Temperature (°C)

### Supported Patient Profiles
- Normal Adult
- Hypertensive Adult
- Hypotensive Adult
- Child

Each profile produces vitals within realistic physiological ranges and supports controlled abnormal spikes for demonstration purposes.


## 4. Patient Baseline Modeling

Each patient is assigned a **personal baseline range** for every vital sign. These baselines may differ based on:
- Age group
- Medical condition
- Patient type

Incoming vitals are evaluated **relative to the patient’s own baseline**, not a fixed universal threshold.


## 5. Outlier Detection Logic

Outlier detection is performed using a hybrid approach:

### Rule-Based Detection
- Checks if vitals fall outside patient-specific baseline ranges

### Machine Learning-Based Risk Scoring
- Random Forest and XGBoost models trained on historical vitals
- Generates a probabilistic risk score

An abnormal event is flagged if:
- One or more vitals deviate from baseline
- OR ML risk score exceeds a predefined threshold


## 6. Alert Generation

When an abnormal condition is detected, the server generates an alert containing:
- Patient ID
- Patient type
- Deviating vitals
- Risk score
- Timestamp

Alerts are stored temporarily and made available to the dashboard for real-time visualization.


## 7. Dashboard Integration

The dashboard continuously polls the server and displays:
- Live vitals streams
- Frequency-based line graphs
- Alert status (Normal / Critical)
- Textual alert messages for doctors

The dashboard is designed to be simple, readable, and suitable for clinical demonstrations.


## 8. Experimental Validation

The system was validated through:
- Continuous real-time simulation
- Forced abnormal vitals
- Multi-patient testing
- Live alert verification on the dashboard

The alert pipeline was confirmed to function within seconds of abnormality occurrence.


## 9. Applications

- ICU monitoring system prototypes
- Remote patient monitoring demos
- Healthcare IoT system testing
- Clinical decision support simulations
- Academic and hackathon projects


## 10. Limitations

- Simulated data does not fully capture real sensor noise
- No hardware integration in current version
- Alert thresholds require clinical tuning


## 11. Future Work

- Integration with wearable sensors
- Time-series anomaly detection models
- Multi-patient dashboard scaling
- Doctor mobile notifications
- Electronic Health Record (EHR) integration


Author  
Subha Tharani  
AI/ML | Healthcare Systems

