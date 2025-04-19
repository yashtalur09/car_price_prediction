
import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('car_price_predictor')  # Replace 'car_price_predictor' with your model file name

# Define the prediction function
def predict_car_price(Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, Age):
    """
    Predicts the car price using the loaded model.

    Args:
        Present_Price (float): The current price of the car.
        Kms_Driven (float): The kilometers driven by the car.
        Fuel_Type (int): The fuel type of the car (0: Petrol, 1: Diesel, 2: CNG).
        Seller_Type (int): The type of seller (0: Dealer, 1: Individual).
        Transmission (int): The transmission type (0: Manual, 1: Automatic).
        Owner (int): The number of previous owners.
        Age (int): The age of the car.

    Returns:
        float: The predicted price of the car.
    """
    data_new = pd.DataFrame({
        'Present_Price': [Present_Price],
        'Kms_Driven': [Kms_Driven],
        'Fuel_Type': [Fuel_Type],
        'Seller_Type': [Seller_Type],
        'Transmission': [Transmission],
        'Owner': [Owner],
        'Age': [Age]
    })
    result = model.predict(data_new)
    return result[0]

# Streamlit app
st.title("Car Price Prediction")

# Input fields
Present_Price = st.number_input("Enter Present Price", value=0.0)
Kms_Driven = st.number_input("Enter Kilometers Driven", value=0)
Fuel_Type = st.selectbox("Select Fuel Type", ["Petrol", "Diesel", "CNG"], index=0)
Seller_Type = st.selectbox("Select Seller Type", ["Dealer", "Individual"], index=0)
Transmission = st.selectbox("Select Transmission", ["Manual", "Automatic"], index=0)
Owner = st.number_input("Enter Number of Owners", value=0)
Age = st.number_input("Enter Age of Car", value=0)

# Convert categorical inputs to numerical
Fuel_Type = {"Petrol": 0, "Diesel": 1, "CNG": 2}[Fuel_Type]
Seller_Type = {"Dealer": 0, "Individual": 1}[Seller_Type]
Transmission = {"Manual": 0, "Automatic": 1}[Transmission]

# Prediction button
if st.button("Predict"):
    predicted_price = predict_car_price(Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, Age)
    st.success(f"Predicted Car Purchase Amount: **{predicted_price:.2f}k**")