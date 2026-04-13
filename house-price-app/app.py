import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("home_model.pkl")

st.title("🏠 House Price Prediction")

# Input fields
area = st.number_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms", min_value=1)
age = st.number_input("Age of house")
bathrooms = st.number_input("Bathrooms", min_value=1)
parking = st.number_input("Parking", min_value=0)

location = st.selectbox("Location", ["Urban", "Semi-Urban"])

# Convert location
location_urban = 1 if location == "Urban" else 0

# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "age": age,
        "bathrooms": bathrooms,
        "parking": parking,
        "location_Urban": location_urban
    }])

    prediction = model.predict(input_data)

    st.success(f"Predicted Price: {prediction[0]:.2f}")
