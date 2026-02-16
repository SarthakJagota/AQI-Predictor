# 🌍 AQI Early Warning & Environmental Planning System

## 📌 Overview

This project is a Machine Learning based Air Quality Index (AQI) Prediction System developed using Random Forest Regression and deployed using Streamlit.

The system not only predicts AQI based on pollutant levels but also provides:

- 🚨 Early Warning Alerts  
- 📊 Risk Classification  
- 📈 Pollution Driver Analysis  
- 🌿 Data-Driven Environmental Planning Recommendations  

This transforms a basic ML model into a decision-support system for environmental monitoring.

---

## 🎯 Objectives

- Predict AQI using key pollutant concentrations
- Implement an early warning mechanism
- Identify major pollution contributors
- Support data-driven environmental planning

---

## 🧠 Machine Learning Model

Algorithm: Random Forest Regressor  

Input Features:
- PM2.5
- PM10
- NO2
- SO2
- CO
- O3

Output:
- Predicted AQI Value

---

## 🚨 Early Warning Mechanism

Based on predicted AQI values, the system classifies air quality into:

- 🟢 Good
- 🟡 Moderate
- 🟠 Unhealthy for Sensitive Groups
- 🔴 Unhealthy
- 🟣 Hazardous

Each level triggers contextual health advisories and warning alerts.

---

## 📈 Data-Driven Environmental Planning

The system uses Random Forest feature importance to:

- Identify primary pollution drivers
- Provide actionable policy recommendations
- Support emission monitoring strategies

---

## 🛠 Tech Stack

- Python
- Scikit-learn
- Streamlit
- NumPy
- Pandas
- Joblib
- Google Drive (Model Hosting)

---

## 📂 Project Structure

aqi-predictor/
│
├── app.py
├── requirements.txt
├── README.md
└── (Model downloaded from Google Drive)

---

## ▶️ Running Locally

1. Clone the repository
2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

streamlit run app.py

---

## 🌐 Deployment

The application is deployed using Streamlit Cloud.
The trained model is hosted on Google Drive and automatically downloaded during runtime.

---

## 📊 Model Evaluation Metrics

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## 💡 Future Enhancements

- Time-series AQI forecasting
- Real-time API integration
- Geographic visualization
- Automated alert notifications
- Historical trend dashboard

---

## 👨‍💻 Author

Developed as a college major project and portfolio-ready ML deployment system.
