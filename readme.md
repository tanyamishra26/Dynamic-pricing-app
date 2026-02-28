# Dynamic Surge Pricing & Fare Optimization System

This repository contains the Streamlit deployment layer for the Intelligent Surge Pricing & Dynamic Fare Optimization System.
The application provides a clean, user-facing interface to estimate ride fares in real time by combining:
- A pre-trained surge prediction model
- Contextual weather data
- Rule-based pricing logic
The machine learning complexity is fully abstracted from the end user.
---

## App Overview

The Streamlit app simulates how modern ride-hailing platforms generate fare estimates dynamically.
### What the App Does
- Collects trip details from the user
- Fetches contextual weather data
- Builds model-ready features internally
- Predicts surge multiplier using a pre-trained stacking model
- Applies business pricing rules
- Displays an estimated fare range
- All ML logic runs behind the scenes to ensure a seamless user experience.
## Live Demo

**Deployed Application:**  
[Dynamic-pricing-app – Streamlit App](https://dynamicpricingapp.streamlit.app/)

---

## User Interface
### User Inputs

- Pickup Zone
- Drop Zone
- Trip Distance (km)
- Estimated Travel Time (minutes)

### App Outputs
- Predicted Surge Multiplier
- Estimated Fare Range

---
## App Execution Flow
```
User Input
   ↓
Weather Context Fetch (OpenWeather API)
   ↓
Feature Builder (Internal Processing)
   ↓
Surge Prediction (Stacking Ensemble Model)
   ↓
Pricing Engine (Rule-Based Logic)
   ↓
Fare Range Display
```
---

## Project Structure

```
DSP_APP/
├── utils/
│   ├── feature_builder.py     # Feature engineering logic
│   ├──pricing.py             # Fare calculation logic
│   ├──weather.py             # Weather retrieval logic
│   └── weather.csv            # Historical weather dataset
│
├── app.py                     # Streamlit application
├── surge_pricing_model.pkl    # Trained ML pipeline
├── requirements.txt           # Dependencies
└── readme.md

```


---


## Deployment

The model is deployed using **Streamlit**.

### Key Deployment Design Decisions:

- Modular utility structure (`utils/`)
- Preprocessing inside pipeline
- Weather pulled from historical dataset
- Explicit missing value handling
- Separation of ML logic and pricing engine

---

##  Run Locally

### Clone the repository

```bash
git clone https://github.com/tanyamishra26/Dynamic-pricing-app
cd DSP_APP
```
### Install dependencies

```bash
pip install -r requirements.txt
```
### Run the app
```bash
streamlit run app.py
```
## Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

## Author

Tanya Mishra
