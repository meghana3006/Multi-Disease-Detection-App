import streamlit as st
import numpy as np
import pickle


def run():

    # ----------------------------------
    # Page config
    # ----------------------------------

    st.title("🫘 Kidney Disease Detection")
    st.write("Enter the patient clinical details to detect kidney disease.")

    # ----------------------------------
    # Load model and scaler
    # ----------------------------------
    # Load model & scaler
    model = pickle.load(open('kidneymodel.pkl', 'rb'))
    scaler = pickle.load(open('kidneyscaler.pkl', 'rb'))


    # ----------------------------------
    # Feature inputs
    # ----------------------------------
    feature_inputs = {
        'Age': st.number_input('Age', min_value=1, value=40),
        'Blood Pressure': st.number_input('Blood Pressure', min_value=50.0, value=120.0),
        'Blood glucose': st.number_input('Blood glucose', min_value=50.0, value=100.0),
        'Serum creatinine': st.number_input('Serum creatinine', min_value=0.1, value=1.0),
        'Blood urea': st.number_input('Blood urea', min_value=5.0, value=40.0),
        'Albumin': st.number_input('Albumin', min_value=0.0, value=4.0),
        'Sodium': st.number_input('Sodium', min_value=110.0, value=140.0),
        'potassium': st.number_input('potassium', min_value=2.0, value=4.5),
        'hemoglobin': st.number_input('hemoglobin', min_value=3.0, value=13.0),
        'Edema': st.number_input('Edema', min_value=0, max_value=1, value=1),
    }

    # Maintain correct feature order
    feature_names = list(feature_inputs.keys())
    input_values = [feature_inputs[f] for f in feature_names]

    # ----------------------------------
    # Prediction
    # ----------------------------------
    if st.button("Detect"):

        input_array = np.array(input_values).reshape(1, -1)

        # Scale input
        scaled_input = scaler.transform(input_array)

        # Predict
        prediction = model.predict(scaled_input)

        result = "Yes" if prediction[0] == 1 else "No"

        st.success(f"🩺 Do you have Kidney Disease: **{result}**")


