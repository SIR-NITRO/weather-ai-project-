import streamlit as st
import pandas as pd

st.title("Weather Prediction App")
st.write("This app predicts weather using machine learning")

# Add a simple input
temperature = st.slider("Temperature (°C)", -10, 40, 20)
st.write(f"Selected temperature: {temperature}°C")












