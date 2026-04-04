# 🏥 Insurance Premium Prediction App

An end-to-end Machine Learning application that predicts insurance premium categories based on user demographics and lifestyle data. This project features a **FastAPI inference engine** for real-time predictions and a **Streamlit web interface** for user interaction.



---

## 🚀 Features
* **Automated Feature Engineering:** Calculates BMI, Age Group, and Lifestyle Risk on-the-fly using Pydantic `computed_field`.
* **Robust Data Validation:** Strict schema enforcement using `Annotated` types (e.g., Age constraints: 0-120).
* **Real-time Inference:** A RESTful API that handles JSON requests and returns class probabilities.
* **Interactive UI:** A clean Streamlit dashboard for easy user input and result visualization.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Modeling:** Scikit-Learn, Pandas, NumPy
* **Backend:** FastAPI, Uvicorn
* **Validation:** Pydantic v2
* **Frontend:** Streamlit
* **Serialization:** Pickle

---

## 📁 Project Structure
```text
.
├── main.py              # FastAPI Inference Server
├── app.py               # Streamlit Frontend
├── model.pkl            # Trained ML Model (Random Forest/XGBoost)
├── config.py            # City Tier & Constants configuration
├── notebook.ipynb       # EDA and Model Training Script
└── requirements.txt     # Project Dependencies
