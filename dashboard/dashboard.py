import streamlit as st
import requests
import time

SERVER = "http://127.0.0.1:8000/dashboard"

st.set_page_config(page_title="Live Vitals", layout="wide")
st.title("🩺 Live Vitals Monitoring Dashboard")

placeholder = st.empty()

while True:
    try:
        data = requests.get(SERVER).json()

        if not data:
            placeholder.warning("Waiting for vitals...")
        else:
            latest = data[-1]

            if latest["alert"]:
                placeholder.error("🚨 ABNORMAL VITALS DETECTED")
                st.warning("🔔 Doctor Alert!")
            else:
                placeholder.success("✅ Patient Stable")

            st.metric("Heart Rate", latest["heart_rate"])
            st.metric("SpO₂", latest["spo2"])
            st.metric("Temperature", latest["temperature"])
            st.metric("BP", f'{latest["systolic"]}/{latest["diastolic"]}')

    except:
        st.error("Server not reachable")

    time.sleep(2)
    st.rerun()
