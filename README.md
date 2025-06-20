# 💼 HR Attrition Predictor - Interactive ML App with Explainability

This project presents an explainable machine learning solution to help HR teams identify employees at risk of leaving the company. Built using XGBoost, Streamlit, and SHAP, it combines predictive accuracy with interpretability.

---

## 🚀 Live App  
🔗 [Launch the HR Attrition Predictor](https://hr-attrition-predictor-acme6nm34kgx8yvxz3yvvq.streamlit.app/)

---

## 🎯 Objective

- Predict whether an employee is likely to leave (Attrition: Yes/No)
- Provide visual explanations for each prediction
- Empower HR to take proactive retention measures

---

## 📊 Key Features

- Input employee details through a user-friendly form
- Get real-time prediction results (Yes / No)
- View SHAP plots explaining **why** the prediction was made

---

## 🧠 Model Details

- **Algorithm**: XGBoost Classifier  
- **Preprocessing**: One-hot encoding, feature scaling  
- **Handling Class Imbalance**: SMOTE  
- **Explainability**: SHAP (SHapley Additive Explanations)  
- **Key Drivers**: OverTime, JobSatisfaction, DistanceFromHome, StockOptionLevel

---

## 🛠️ Tools & Technologies

- Python, Pandas, Scikit-learn, Imbalanced-learn  
- XGBoost, SHAP  
- Streamlit for frontend deployment

---

## 📁 Files

- `HR_Analytics_Model.ipynb` – Model training pipeline  
- `app.py` – Streamlit app  
- `models/` – Saved model, scaler, and features  
- `requirements.txt` – Dependency list

---

## 📸 Screenshots

| Form Input | Prediction Output | SHAP Explanation |
|------------|-------------------|------------------|
| ![Form Input](assets/form-input.png) | ![Prediction](assets/prediction-result.png) | ![SHAP](assets/shab-plot.png) |

---

## ✅ Author  
**Shauryaditya Singh**  
Aspiring Data Scientist | Explainable AI Enthusiast

