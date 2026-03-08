import streamlit as st
import numpy as np
import pickle


def run():


    # Load model & scaler
    model = pickle.load(open('breastcancermodel.pkl', 'rb'))
    scaler = pickle.load(open('breastcancerscaler.pkl', 'rb'))

    st.title("Breast Cancer Detection")
    st.write("Enter the values for the following features:")

    radius_mean = st.number_input("Radius Mean", value=14.0)
    texture_mean = st.number_input("Texture Mean", value=19.0)
    perimeter_mean = st.number_input("perimeter_mean", value=90.0)
    area_mean = st.number_input("area_mean", value=600.0)
    smoothness_mean = st.number_input("smoothness_mean", value=0.1)
    compactness_mean = st.number_input("compactness_mean", value=0.1)
    concavity_mean = st.number_input("concavity_mean", value=0.1)
    concave_points_mean = st.number_input("concave points_mean", value=0.05)
    symmetry_mean = st.number_input("symmetry_mean", value=0.18)
    fractal_dimension_mean = st.number_input("fractal_dimension_mean", value=0.06)

    # ===== SE Features =====
    radius_se = st.number_input('radius_se', value=0.4)
    texture_se = st.number_input('texture_se', value=1.2)
    perimeter_se = st.number_input('perimeter_se', value=2.8)
    area_se = st.number_input('area_se', value=40.0)
    smoothness_se = st.number_input('smoothness_se', value=0.007)
    compactness_se = st.number_input('compactness_se', value=0.025)
    concavity_se = st.number_input('concavity_se', value=0.03)
    concave_points_se = st.number_input('concave points_se', value=0.01)
    symmetry_se = st.number_input('symmetry_se', value=0.02)
    fractal_dimension_se = st.number_input('fractal_dimension_se', value=0.003)


    radius_worst = st.number_input("radius_worst", value=16.0)
    texture_worst = st.number_input("texture_worst", value=25.0)
    perimeter_worst = st.number_input("perimeter_worst", value=110.0)
    area_worst = st.number_input("area_worst", value=800.0)
    smoothness_worst = st.number_input("smoothness_worst", value=0.15)
    compactness_worst = st.number_input("compactness_worst", value=0.25)
    concavity_worst = st.number_input("concavity_worst", value=0.3)
    concave_points_worst = st.number_input("concave points_worst", value=0.1)
    symmetry_worst = st.number_input("symmetry_worst", value=0.3)
    fractal_dimension_worst = st.number_input("fractal_dimension_worst", value=0.08)

    

    if st.button("Detect"):

        input_data = np.array([[ 
            radius_mean, texture_mean, perimeter_mean, area_mean,
            smoothness_mean, compactness_mean, concavity_mean,
            concave_points_mean, symmetry_mean, fractal_dimension_mean,
            radius_se, texture_se, perimeter_se, area_se, smoothness_se,
            compactness_se, concavity_se, concave_points_se, symmetry_se,
            fractal_dimension_se, radius_worst, texture_worst,
            perimeter_worst, area_worst, smoothness_worst,
            compactness_worst, concavity_worst, concave_points_worst,
            symmetry_worst, fractal_dimension_worst
        ]])

        # Apply scaling
        scaled_input = scaler.transform(input_data)

        prediction = model.predict(scaled_input)

        if prediction[0] == 0:
            st.error("The tumor is Benign")
        else:
            st.success("The tumor is Maligant")


