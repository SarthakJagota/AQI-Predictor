import streamlit as st
import numpy as np
import pandas as pd
import os
import gdown
import joblib

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="AQI Early Warning System",
    page_icon="🌍",
    layout="wide"
)

# -------------------------------------------------
# Styling
# -------------------------------------------------
st.markdown("""
    <style>
    .main-title {
        font-size:42px;
        font-weight:700;
        text-align:center;
        color:#1f4e79;
    }
    .subtitle {
        text-align:center;
        font-size:18px;
        color:gray;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown('<p class="main-title">🌍 AQI Prediction & Early Warning System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Machine Learning Driven Environmental Decision Support Tool</p>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# Load Model from Google Drive
# -------------------------------------------------
MODEL_PATH = "aqi_model.pkl"

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1_Lb_PjtXrgFeCfewKOhJ1hVp5N_V4mAm"
    gdown.download(url, MODEL_PATH, quiet=False)

model = joblib.load(MODEL_PATH)

# -------------------------------------------------
# Input Section
# -------------------------------------------------
st.subheader("📥 Enter Pollutant Levels")

col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.slider("PM2.5", 0.0, 500.0, 50.0)
    pm10 = st.slider("PM10", 0.0, 500.0, 80.0)

with col2:
    no2 = st.slider("NO2", 0.0, 300.0, 40.0)
    so2 = st.slider("SO2", 0.0, 200.0, 20.0)

with col3:
    co = st.slider("CO", 0.0, 10.0, 1.0)
    o3 = st.slider("O3", 0.0, 300.0, 30.0)

st.divider()

# -------------------------------------------------
# Prediction
# -------------------------------------------------
if st.button("🔮 Predict AQI", use_container_width=True):

    input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
    prediction = model.predict(input_data)[0]
    prediction = round(prediction, 2)

    st.subheader("📊 Predicted AQI")

    col_a, col_b, col_c = st.columns([1,2,1])
    with col_b:
        st.metric("AQI Value", prediction)

    st.divider()

    # -------------------------------------------------
    # Early Warning Classification
    # -------------------------------------------------
    st.subheader("🚨 Early Warning Assessment")

    if prediction <= 50:
        st.success("🟢 Good Air Quality")
        st.info("Minimal health risk.")
    elif prediction <= 100:
        st.info("🟡 Moderate Air Quality")
        st.warning("Sensitive individuals should limit prolonged outdoor exposure.")
    elif prediction <= 200:
        st.warning("🟠 Unhealthy for Sensitive Groups")
        st.error("⚠ Early Warning: Preventive measures advised.")
    elif prediction <= 300:
        st.error("🔴 Unhealthy")
        st.error("🚨 ALERT: Avoid outdoor exposure.")
    else:
        st.error("🟣 Hazardous")
        st.error("🚨 CRITICAL ALERT: Immediate intervention required.")

    st.divider()

    # -------------------------------------------------
    # 1️⃣ Model-Based Global Importance
    # -------------------------------------------------
    st.subheader("📈 Model-Based Pollution Influence")

    feature_names = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
    importance = model.feature_importances_

    importance_df = pd.DataFrame({
        "Pollutant": feature_names,
        "Model Importance": importance
    }).sort_values(by="Model Importance", ascending=False)

    st.bar_chart(importance_df.set_index("Pollutant"))

    model_dominant = importance_df.iloc[0]["Pollutant"]
    st.write(f"Model-identified dominant pollutant: **{model_dominant}**")

    st.divider()

    # -------------------------------------------------
    # 2️⃣ Real-Time Exceedance Analysis
    # -------------------------------------------------
    st.subheader("📊 Real-Time Pollution Stress Analysis")

    safe_limits = {
        "PM2.5": 50,
        "PM10": 100,
        "NO2": 40,
        "SO2": 40,
        "CO": 2,
        "O3": 100
    }

    input_values = {
        "PM2.5": pm25,
        "PM10": pm10,
        "NO2": no2,
        "SO2": so2,
        "CO": co,
        "O3": o3
    }

    exceedance_ratio = {
        key: input_values[key] / safe_limits[key]
        for key in input_values
    }

    exceed_df = pd.DataFrame({
        "Pollutant": exceedance_ratio.keys(),
        "Exceedance Ratio": exceedance_ratio.values()
    }).sort_values(by="Exceedance Ratio", ascending=False)

    st.bar_chart(exceed_df.set_index("Pollutant"))

    current_critical = exceed_df.iloc[0]["Pollutant"]
    st.write(f"Current critical pollutant (based on safety threshold exceedance): **{current_critical}**")

    st.divider()

    # -------------------------------------------------
    # Planning Recommendation
    # -------------------------------------------------
    st.subheader("🌿 Environmental Planning Recommendation")

    if current_critical == "PM2.5":
        st.write("Recommended Action: Control construction dust and vehicular emissions.")
    elif current_critical == "NO2":
        st.write("Recommended Action: Regulate traffic and combustion sources.")
    elif current_critical == "SO2":
        st.write("Recommended Action: Monitor coal-based industries and power plants.")
    elif current_critical == "CO":
        st.write("Recommended Action: Strengthen vehicle emission inspections.")
    elif current_critical == "O3":
        st.write("Recommended Action: Reduce NOx and VOC emissions.")

st.divider()
st.caption("Random Forest Regression | Early Warning Environmental Decision System")
