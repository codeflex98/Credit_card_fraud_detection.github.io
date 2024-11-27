import streamlit as st
import numpy as np
import pandas as pd
import os
import joblib

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'credit_card_Fraud_detection_model')
model = joblib.load(model_path)
# App title and description
st.title("Credit Card Fraud Detection")
st.write("This app predicts whether a credit card transaction is fraudulent or not based on the provided inputs.")

# Input form for user features
st.sidebar.header("Transaction Details")
p1 = st.number_input("V1",min_value=-5, max_value=5, format="%0.4f")
p2 = st.number_input("V2",min_value=-5, max_value=5, format="%0.4f")
p3 = st.number_input("V3",min_value=-5, max_value=5, format="%0.4f")
p4 = st.number_input("V4",min_value=-5, max_value=5, format="%0.4f")
p5 = st.number_input("V5",min_value=-5, max_value=5, format="%0.4f")
p6 = st.number_input("V6",min_value=-5, max_value=5, format="%0.4f")
p7 = st.number_input("V7",min_value=-5, max_value=5, format="%0.4f")
p8 = st.number_input("V8",min_value=-5, max_value=5, format="%0.4f")
p9 = st.number_input("V9",min_value=-5, max_value=5, format="%0.4f")
p10 = st.number_input("V10",min_value=-5, max_value=5, format="%0.4f")
p11 = st.number_input("V11",min_value=-5, max_value=5, format="%0.4f")
p12 = st.number_input("V12",min_value=-5, max_value=5, format="%0.4f")
p13 = st.number_input("V13",min_value=-5, max_value=5, format="%0.4f")
p14 = st.number_input("V14",min_value=-5, max_value=5, format="%0.4f")
p15 = st.number_input("V15",min_value=-5, max_value=5, format="%0.4f")
p16 = st.number_input("V16",min_value=-5, max_value=5, format="%0.4f")
p17 = st.number_input("V17",min_value=-5, max_value=5, format="%0.4f")
p18 = st.number_input("V18",min_value=-5, max_value=5, format="%0.4f")
p19 = st.number_input("V19",min_value=-5, max_value=5, format="%0.4f")
p20 = st.number_input("V20",min_value=-5, max_value=5, format="%0.4f")
p21 = st.number_input("V21",min_value=-5, max_value=5, format="%0.4f")
p22 = st.number_input("V22",min_value=-5, max_value=5, format="%0.4f")
p23 = st.number_input("V23",min_value=-5, max_value=5, format="%0.4f")
p24 = st.number_input("V24",min_value=-5, max_value=5, format="%0.4f")
p25 = st.number_input("V25",min_value=-5, max_value=5, format="%0.4f")
p26 = st.number_input("V26",min_value=-5, max_value=5, format="%0.4f")
p27 = st.number_input("V27",min_value=-5, max_value=5, format="%0.4f")
p28 = st.number_input("V28",min_value=-5, max_value=5, format="%0.4f")
p29 = st.number_input("Amount",min_value=0, max_value=100000)

# Debugging statements
#print(f"Inputs: {p1}, {p2}, {p3}, {p4}, {p5}, {p6}, {p7}, {p8}, {p9}, {p10}, {p11}, {p12} {p13}, {p14}, {p15}")
input_data = np.array([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29]])
print(f"Input data shape: {input_data.shape}")

# Button to trigger prediction
if st.sidebar.button("Predict"):
    prediction = model.predict(input_data)[0]  # Assuming binary classification (0 or 1)
    prediction_proba = model.predict_proba(input_data)[0]

    # Display results
    if prediction == 0:
        st.success(f"The transaction is predicted to be Non-Fraudulent with a probability of {prediction_proba[0]:.2f}.")
    else:
        st.error(f"The transaction is predicted to be Fraudulent with a probability of {prediction_proba[1]:.2f}.")