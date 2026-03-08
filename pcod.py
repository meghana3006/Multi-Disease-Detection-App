import streamlit as st
import numpy as np
import pickle


def run():

    # ----------------------------------
    # Page config
    # ----------------------------------
    
    st.title("PCOD Detection")
    st.write("Enter the details to detect PCOD.")

    # ----------------------------------
    # Load model and scaler
    # ----------------------------------
    # Load model & scaler
    model = pickle.load(open('pcodmodel.pkl', 'rb'))
    scaler = pickle.load(open('pcodscaler.pkl', 'rb'))


   
    # ----------------------------------
    # Feature inputs
    # ----------------------------------
    feature_inputs = {
        'number_of_peak': st.number_input('Number_of_peak', min_value=0, value=5),
        'Age': st.number_input('Age', min_value=0, value=25),
        'Length_of_cycle': st.number_input('Length_of_cycle', min_value=0, value=28),
        'Estimated_day_of_ovulution': st.number_input('Estimated_day_of_ovulution', min_value=0, value=14),
        'Length_of_Gap': st.number_input('Length_of_Gap', min_value=0, value=5),
        'Length_of_menses': st.number_input('Length_of_menses', min_value=0, value=5),
        'Weight': st.number_input('Weight', min_value=0, value=60),
        'Mean_of_length_of_cycle': st.number_input('Mean_of_length_of_cycle', min_value=0, value=28),
        'Menses_score': st.number_input('Menses_score', min_value=0, value=3),
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

        result = "PCOD Positive" if prediction[0] == 1 else "PCOD Negative"

        st.success(f"PCOD Detection Result: **{result}**")


