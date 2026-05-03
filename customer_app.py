import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("kmeans.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🛒 Ecommerce Customer Segmentation")

st.write("Enter Customer Details")

# Inputs
recency = st.number_input("Recency (days)")
frequency = st.number_input("Frequency (transactions)")
monetary = st.number_input("Monetary (total spend)")

if st.button("Predict Customer Segment"):

    data = scaler.transform([[recency, frequency, monetary]])
    cluster = model.predict(data)[0]

    # Cluster meaning
    if cluster == 0:
        result = "High Value Customer 💰"
    elif cluster == 1:
        result = "Low Value Customer"
    elif cluster == 2:
        result = "Frequent Buyer 🛒"
    else:
        result = "At Risk Customer ⚠️"

    st.success(f"Customer belongs to Cluster {cluster}")
    st.write(f"Category: {result}")