# streamlit_app.py

import streamlit as st
import pandas as pd
import joblib
import shap
import numpy as np

# Load model, scaler, and feature names
model = joblib.load("models/xgb_attrition_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")

st.set_page_config(page_title="Attrition Predictor")
st.title("Employee Attrition Predictor")

st.write("Fill in the details below to assess if an employee is likely to leave.")

# Input form
with st.form("input_form"):
    Age = st.slider("Age", 18, 60, 30)
    MonthlyIncome = st.number_input("Monthly Income", min_value=1000, max_value=20000, value=5000)
    DistanceFromHome = st.slider("Distance from Home (km)", 1, 50, 5)
    OverTime_Yes = st.selectbox("Does the employee work overtime?", ["Yes", "No"])
    JobSatisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
    JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    NumCompaniesWorked = st.slider("No. of Companies Worked At", 0, 10, 2)
    StockOptionLevel = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    YearsSinceLastPromotion = st.slider("Years Since Last Promotion", 0, 15, 2)
    WorkLifeBalance = st.slider("Work-Life Balance (1-4)", 1, 4, 3)

    submitted = st.form_submit_button("Predict")

if submitted:
    # Prepare input
    data = {
        "Age": Age,
        "MonthlyIncome": MonthlyIncome,
        "DistanceFromHome": DistanceFromHome,
        "OverTime_Yes": 1 if OverTime_Yes == "Yes" else 0,
        "JobSatisfaction": JobSatisfaction,
        "JobLevel": JobLevel,
        "NumCompaniesWorked": NumCompaniesWorked,
        "StockOptionLevel": StockOptionLevel,
        "YearsSinceLastPromotion": YearsSinceLastPromotion,
        "WorkLifeBalance": WorkLifeBalance
    }

    df = pd.DataFrame([data])

    # Ensure correct column order
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0
    df = df[feature_names]

    # Scale + predict
    scaled = scaler.transform(df)
    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]

    st.subheader("Result:")
    if prediction == 1:
        st.error(f"⚠️ High Risk of Attrition (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low Risk of Attrition (Probability: {probability:.2f})")

    # SHAP Explanation
    explainer = shap.Explainer(model)
    shap_values = explainer(scaled)
    st.subheader("SHAP Explanation")
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    # Generate SHAP plot
    shap.plots.waterfall(shap_values[0], show=False)
    # Get the current figure (from SHAP's internal plotting)
    fig = plt.gcf()
    st.pyplot(fig)

