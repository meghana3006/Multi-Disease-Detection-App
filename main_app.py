import streamlit as st
st.set_page_config(
    
    page_title="Multi Disease Detection System",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
    </style>
""", unsafe_allow_html=True)


import diabetes
import breastcancer
import kidney
import lungcancer
import pcod


# Sidebar Menu
st.sidebar.title("🏥 Disease Detection System")

app_mode = st.sidebar.selectbox(
    "Select Disease",
    ["Home", "Breast Cancer Detection", "Diabetes Detection","Kidney Condition Detection","Lung Cancer Detection","PCOD Detection"]
)
st.sidebar.title("👩‍💻 Team Members")

st.sidebar.markdown("""
- **Satti Asritha Reddy**
- **Meghana Mupparthi**
- **Tejaswi Swarna**
- **Puredla Nayana**
""")
st.sidebar.subheader("🎓 Guided By")
st.sidebar.markdown("""
- **Abdul Aziz Md**  
""")
st.title("AICW(Artificial Intelligence For Women)")
st.markdown("""
          <h5 style='text-align:center;padding-bottom:0'>CSR initiative by Microsoft and SAP</h5>,
             <h5 style='text-align:center;padding-top:0'>In collaboration with Edunet foundation</h5>""",unsafe_allow_html=True)

# Navigation
if app_mode == "Home":
    
    st.title("🏥 Multi Disease Detection App")
    st.write("""
    This application Detects multiple diseases using Machine Learning.
    
    Select a disease from the sidebar to begin.
    """)
    import streamlit as st
    from PIL import Image


    # image = Image.open("picture1.jpg")   # your image file name
    # col1, col2, col3 = st.columns([1,6,1])

    # with col2:
    #     st.image("picture1.jpg", width=500)

    import os

    # Get the path of the current script
    script_dir = os.path.dirname(__file__)
    # Create the full path to the image
    img_path = os.path.join(script_dir, "picture1.jpg")

    # Open and display the image using the full path
    if os.path.exists(img_path):
        image = Image.open(img_path)
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            st.image(image, width=500)
    else:
        st.error(f"Image not found! Looking for: {img_path}")
        st.write("these are the files belong to folder")
        st.write("os.listdir(script_dir"))


elif app_mode == "Diabetes Detection":
    diabetes.run()


elif app_mode == "Breast Cancer Detection":
    breastcancer.run()

elif app_mode == "Kidney Condition Detection":
    kidney.run()

elif app_mode == "Lung Cancer Detection":
    lungcancer.run()    

elif app_mode == "PCOD Detection":
    pcod.run()






