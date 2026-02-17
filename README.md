# 🌍 Smart AQI Early Warning & Environmental Planning System

## 📌 Overview

This project is a Machine Learning powered Air Quality Index (AQI) Prediction and Decision Support System developed using supervised regression models and deployed with Streamlit.

The system predicts AQI from pollutant concentrations and transforms predictions into:

- 🚨 Early Warning Alerts  
- 📊 Risk Level Classification  
- 📈 Pollution Driver Analysis  
- 🌿 Data-Driven Environmental Planning Recommendations  

It goes beyond simple prediction and acts as an environmental intelligence dashboard.

---

## 🎯 Objectives

- Predict AQI using major pollutant concentrations  
- Compare multiple regression models  
- Implement an early warning mechanism  
- Identify key pollution contributors  
- Support data-driven environmental policy decisions  

---

## 🧠 Machine Learning Pipeline

### Models Trained

- Linear Regression (Baseline)
- Random Forest Regressor
- XGBoost Regressor (Final Model)

### Final Model Selected

**XGBoost Regressor**  
Achieved highest R² score (~92%).

### Input Features

- PM2.5  
- PM10  
- NO  
- NO2  
- NOx  
- CO  
- O3  

### Output

- Predicted AQI Value  

---

## 📊 Model Performance

| Model               | R² Score |
|--------------------|----------|
| Linear Regression  | ~0.85    |
| Random Forest      | ~0.91    |
| XGBoost            | ~0.92    |

XGBoost performed best due to its ability to capture nonlinear pollutant interactions.

---

## 🚨 Early Warning Mechanism

Predicted AQI values are categorized into:

- 🟢 Good  
- 🟡 Satisfactory  
- 🟠 Moderate  
- 🔴 Poor  
- 🟣 Very Poor  
- ⚫ Severe  

Each category triggers:

- Health advisory notifications  
- Risk visualization  
- Environmental action recommendations  

---

## 📈 Data-Driven Environmental Planning

Using feature importance from tree-based models, the system:

- Identifies dominant pollution drivers  
- Supports emission reduction strategies  
- Assists smart city planning initiatives  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib  
- Streamlit  
- Joblib  

---

---

## 📊 Evaluation Metrics

- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  

---

## 🌱 Future Enhancements

- Hyperparameter tuning  
- SHAP explainability  
- Time-series AQI forecasting  
- Real-time API integration  
- Geospatial AQI visualization  

---

## 👨‍💻 Author

Developed as a university major project and portfolio-ready Machine Learning deployment system focused on environmental intelligence and smart city applications.


