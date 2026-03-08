import streamlit as st
import numpy as np
import pickle


def run():

    
    # Load model & scaler
    model = pickle.load(open('diabetesmodel.pkl', 'rb'))
    scaler = pickle.load(open('diabetesscaler.pkl', 'rb'))


    st.title("🩺 Diabetes Detection System")

    pregnancies = st.number_input("Pregnancies", min_value=0, value=1)
    glucose = st.number_input("Glucose Level", min_value=0, value=120)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, value=70)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, value=20)
    insulin = st.number_input("Insulin Level", min_value=0, value=80)
    bmi = st.number_input("BMI", min_value=0.0, value=25.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.5)
    age = st.number_input("Age", min_value=1, value=30)

    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi,
                            dpf, age]])

    if st.button("Detect"):

        scaled_input = scaler.transform(input_data)   # 🔥 Important line
        prediction = model.predict(scaled_input)

        if prediction[0] == 1:
            st.error("⚠️ Diabetic")
        else:
            st.success("✅ Non-Diabetic")


