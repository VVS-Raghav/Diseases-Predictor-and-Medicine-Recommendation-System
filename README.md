# Disease Prediction and Health Suggestion Web App

A machine learning-powered web application that predicts diseases based on selected symptoms and suggests relevant precautions, medications, diets, and workouts to aid recovery. The app uses a trained **Random Forest Classifier** and integrates a Python backend with an Express.js frontend.

---

## 🚀 Features

- 🔍 Predicts the most likely disease based on user-input symptoms
- 🩹 Provides a detailed description of the disease
- 💊 Suggests medications and precautions
- 🥗 Recommends diets and workout routines
- 📊 Uses a trained Random Forest model for high accuracy
- 🌐 Simple and interactive web interface using EJS templating

---

## 🧰 Tech Stack

**Frontend**  
- HTML/CSS (via EJS templates)  
- EJS View Engine  

**Backend**  
- Node.js (Express server)  
- Python (ML model and symptom processing)  
- `python-shell` to integrate Python with Node.js  

**Machine Learning**  
- `scikit-learn` for model building  
- `pandas`, `joblib`, `numpy` for preprocessing and I/O  

---

## 🏗️ Folder Structure
.
├── server.js # Express.js server
├── package.json # Node.js project config
├── predict.py # Python script for disease prediction
├── Model training.py # ML model training script
├── /models # Saved ML models
├── /datasets # Symptom and disease datasets
├── /views # EJS templates
├── /public # Static files (CSS, images)
└── symptoms.json # List of symptom options

---

## 🧪 Usage

1. Navigate to the home page.
2. Select symptoms from the provided checklist.
3. Click **Predict**.
4. View:
   - ✅ Predicted disease
   - 📃 Description
   - 🩺 Precautionary steps
   - 💊 Medications
   - 🥗 Diet plans
   - 🏋️ Recommended workouts

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Preprocessing Steps:**
  - Label encoding of disease labels
  - Binary symptom vector creation (one-hot encoding of symptoms)
- **Train/Test Split:** 80% training / 20% testing
- **Accuracy:** Displayed in the console after training via `Model training.py`

---

## 📷 Screenshots

> 

---

## 📄 License

This project is licensed under the **ISC License**, as specified in the `package.json`.


