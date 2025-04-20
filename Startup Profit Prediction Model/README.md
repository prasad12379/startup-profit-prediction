# Startup Profit Prediction System

This project applies **Multiple Linear Regression** to predict the profit of a startup based on various spending features.

---

## Problem Statement

Given data from 50 startups, the goal is to build a machine learning model that can accurately predict profits using R&D Spend, Administration, and Marketing Spend.

---

## Dataset

- **File:** `50_Startups.csv`
- **Features:**
  - `R&D Spend`
  - `Administration`
  - `Marketing Spend`
  - `State` (Categorical)
  - `Profit` (Target)

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib (for visualization)

---

## Files Included

- `startup_profit_prediction.py` – ML pipeline code: preprocessing, training, evaluation
- `50_Startups.csv` – Dataset of 50 startups
- `profit_model.pkl` – Serialized model for future predictions (optional)

---

## Model Performance

- **Algorithm Used:** Multiple Linear Regression
- **Accuracy:** ~93%
- Feature engineering & encoding done for categorical variables.

---

## Future Scope

- Use polynomial regression for nonlinear patterns
- Deploy using Flask/Streamlit for real-time prediction

---

## Author

**Prasad Dhokane**  
 prasaddhokane9@gmail.com  
 [LinkedIn](https://linkedin.com/in/prasad-dhokane-58487728a)
