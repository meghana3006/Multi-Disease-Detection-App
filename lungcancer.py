import streamlit as st
import pickle
import numpy as np


def run():

    # -----------------------------
    # Page Config
    # -----------------------------
    

    st.title("🫁 Lung Cancer Detection")
    st.write("Enter the patient details to predict lung cancer risk.")

    # -----------------------------
    # Load Model & Scaler
    # -----------------------------
    # Load model & scaler
    model = pickle.load(open('lungcancermodel.pkl', 'rb'))
    scaler = pickle.load(open('lungcancerscaler.pkl', 'rb'))


    # -----------------------------
    # User Inputs
    # -----------------------------
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", 1, 100, value=30)

    smoking = st.selectbox("Smoking", [1, 2])
    yellow_fingers = st.selectbox("Yellow Fingers", [1, 2])
    anxiety = st.selectbox("Anxiety", [1, 2])
    peer_pressure = st.selectbox("Peer Pressure", [1, 2])
    chronic = st.selectbox("Chronic Disease", [1, 2])
    fatigue = st.selectbox("Fatigue", [1, 2])
    allergy = st.selectbox("Allergy", [1, 2])
    wheezing = st.selectbox("Wheezing", [1, 2])
    alcohol = st.selectbox("Alcohol Consuming", [1, 2])
    coughing = st.selectbox("Coughing", [1, 2])
    breath = st.selectbox("Shortness of Breath", [1, 2])
    swallow = st.selectbox("Swallowing Difficulty", [1, 2])
    chest_pain = st.selectbox("Chest Pain", [1, 2])

    # Convert gender to numeric
    gender = 0 if gender == "Male" else 1

    # -----------------------------
    # Prediction
    # -----------------------------
    if st.button("Detect"):

        input_data = np.array([[gender, age, smoking, yellow_fingers, anxiety,
                                peer_pressure, chronic, fatigue, allergy,
                                wheezing, alcohol, coughing, breath,
                                swallow, chest_pain]])

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            st.error("⚠️ High Risk of Lung Cancer")
        else:
            st.success("✅ Low Risk of Lung Cancer")


