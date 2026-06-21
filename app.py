import streamlit as st
import pandas as pd
import pickle

# Load model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="House Price Predictor")

st.title("🏠 House Price Prediction")

# Numeric Inputs
area = st.number_input("Area (sq ft)", min_value=500, value=3000)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
stories = st.number_input("Stories", min_value=1, max_value=5, value=2)
parking = st.number_input("Parking", min_value=0, max_value=10, value=1)

# Categorical Inputs
mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["unfurnished", "semi-furnished", "furnished"]
)

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [1 if mainroad == "yes" else 0],
        "guestroom": [1 if guestroom == "yes" else 0],
        "basement": [1 if basement == "yes" else 0],
        "hotwaterheating": [1 if hotwaterheating == "yes" else 0],
        "airconditioning": [1 if airconditioning == "yes" else 0],
        "parking": [parking],
        "prefarea": [1 if prefarea == "yes" else 0],
        "furnishingstatus": [
            0 if furnishingstatus == "unfurnished"
            else 1 if furnishingstatus == "semi-furnished"
            else 2
        ]
    })

    st.write("Input Data:")
    st.dataframe(input_df)

    try:
        prediction = model.predict(input_df)
        st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction Error: {e}")