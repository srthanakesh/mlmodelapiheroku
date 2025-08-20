import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("diabetes_model.sav", "rb"))

st.title("🩺 Diabetes Prediction App")

# Input fields
preg = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glu = st.number_input("Glucose", min_value=0, max_value=300, value=120)
bp = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
ins = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

if st.button("Predict"):
    input_data = np.array([[preg, glu, bp, skin, ins, bmi, dpf, age]])
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.success("✅ The person is NOT diabetic")
    else:
        st.error("⚠️ The person IS diabetic")
