import streamlit as st
import joblib
import pandas as pd
import os

# -----------------------------
# 📂 Load model safely
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "h_model.pkl")

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found! Please upload 'h_model.pkl'")
    st.stop()

model = joblib.load(MODEL_PATH)

# -----------------------------
# 🎨 UI Design
# -----------------------------
st.set_page_config(page_title="House Price Predictor", page_icon="🏠")

st.title("🏠 House Price Prediction App")
st.markdown("### Predict house prices in **Lakhs, Crores & Rupees**")

# -----------------------------
# 📥 User Inputs
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("📐 Area (sq ft)", min_value=0)
    bedrooms = st.number_input("🛏 Bedrooms", min_value=0)
    age = st.number_input("🏚 Age (years)", min_value=0)

with col2:
    bathrooms = st.number_input("🚿 Bathrooms", min_value=0)
    parking = st.number_input("🚗 Parking", min_value=0)
    location = st.selectbox("📍 Location", ["Urban", "Semi-Urban"])

# Encode location
location_Urban = 1 if location == "Urban" else 0

# -----------------------------
# 🔮 Prediction
# -----------------------------
if st.button("🔮 Predict Price"):

    input_data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "age": age,
        "bathrooms": bathrooms,
        "parking": parking,
        "location_Urban": location_Urban
    }])

    try:
        prediction = model.predict(input_data)[0]

        # -----------------------------
        # 💰 Price Formatting
        # -----------------------------
        price_lakhs = prediction
        price_crore = prediction / 100
        price_rupees = prediction * 100000

        # -----------------------------
        # 🎯 Output UI
        # -----------------------------
        st.success(f"💰 Estimated Price: ₹ {price_lakhs:,.2f} Lakhs")

        st.markdown("### 📊 Detailed Breakdown")
        st.write(f"👉 Lakhs: ₹ {price_lakhs:,.2f}")
        st.write(f"👉 Crores: ₹ {price_crore:,.2f}")
        st.write(f"👉 Rupees: ₹ {price_rupees:,.0f}")

    except Exception as e:
        st.error(f"⚠️ Prediction Error: {e}")