import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Load trained model
model = joblib.load("naive_bayes_model.pkl")

# Label mapping (adjust if your encoding was different)
label_map = {
    1: "Safe",
    2: "Intermediate",
    3: "Danger"
}

# Extra custom CSS (keeping sidebar white, modern + colorful look)
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #f9f9fb, #eef2f3);
}

/* Titles */
h1, h2, h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    text-align: center;
    color: #2c3e50;
    margin-bottom: 15px;
}

/* Subheader */
h2, h3 {
    color: #34495e;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #ffffff;
    padding: 20px;
    border-right: 2px solid #e0e0e0;
    box-shadow: 2px 0 8px rgba(0,0,0,0.08);
}

/* Number inputs */
.stNumberInput input {
    border: 1px solid #dcdde1;
    border-radius: 10px;
    padding: 8px;
    background-color: #ffffff;
    color: #2c3e50;
    box-shadow: 0px 3px 6px rgba(0,0,0,0.08);
    transition: 0.3s ease-in-out;
}
.stNumberInput input:focus {
    border-color: #2e86de;
    box-shadow: 0px 4px 10px rgba(46,134,222,0.3);
    outline: none;
}

/* Predict button */
.stButton>button {
    display: inline-block;
    padding: 12px 28px;
    border-radius: 12px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(90deg, #2e86de, #00c6ff);
    color: white;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
}
.stButton>button:hover {
    background: linear-gradient(90deg, #00c6ff, #2e86de);
    transform: scale(1.05);
    box-shadow: 0px 6px 16px rgba(0,0,0,0.25);
}

/* Prediction result box */
.stAlert {
    background: linear-gradient(135deg, #6dd5ed, #2193b0) !important;
    color: white !important;
    border-radius: 12px;
    padding: 15px;
    font-weight: bold;
    font-size: 1.2rem;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* Footer */
footer, .stMarkdown p {
    text-align: center;
    color: #555;
    font-size: 14px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar (Branding Section)
with st.sidebar:
    # Display logo image
    st.image("logo2.png", use_container_width=True)

    # Adding a custom style with HTML and CSS
    st.markdown("""
        <style>
            .custom-text {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                color:#ff0707
            }
            .custom-text span {
                color: #2304f0; /* Color for the word 'Insights' */
            }
        </style>
    """, unsafe_allow_html=True)

    # Displaying the subheader with the custom class
    st.markdown('<p class="custom-text"><span>Smartphone</span> Risk <span>Classifier</span></p>', unsafe_allow_html=True)

    # HTML and CSS for the button
    github_button_html = """
    <div style="text-align: center; margin-top: 50px;">
        <a class="button" href="https://github.com/Engr-Mujeeb-Rahman" target="_blank" rel="noopener noreferrer">Visit my GitHub</a>
    </div>

    <style>
        /* Button styles */
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #02fae9;
            color: black;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #b402fa;
            color: white;
            text-decoration: none; /* Remove underline on hover */
        }

    </style>
    """

    # Display the GitHub button in the app
    st.markdown(github_button_html, unsafe_allow_html=True)
    
    # Footer
    # HTML and CSS for the centered footer
    footer_html = """
    <div style="padding:10px; text-align:center;margin-top: 10px;">
        <p style="font-size:20px; color:#0a0a0a;">Made with ❤️ by Engr. Mujeeb Ur Rahman</p>
    </div>
    """

    # Display footer in the app
    st.markdown(footer_html, unsafe_allow_html=True)

# Main Page (Centered Input Form)
st.title("📱 Smartphone Sensor Risk Classification")
st.write("This app **predicts** the Risk Level (Safe / Intermediate / Danger) of a potential accident based on smartphone sensor data.\n AI-powered system that turns your smartphone into a real-time accident prevention tool")

# Center form layout
with st.form("sensor_form"):
    st.subheader("Enter Sensor Values")

    col1, col2, col3 = st.columns(3)

    with col1:
        x_acc = st.number_input("X Acceleration", value=0.0)
        x_gyro = st.number_input("X Gyroscope", value=0.0)
    with col2:
        y_acc = st.number_input("Y Acceleration", value=0.0)
        y_gyro = st.number_input("Y Gyroscope", value=0.0)
    with col3:
        z_acc = st.number_input("Z Acceleration", value=0.0)
        z_gyro = st.number_input("Z Gyroscope", value=0.0)

    # Derived feature
    acc_magnitude = np.sqrt(x_acc**2 + y_acc**2 + z_acc**2)

    submitted = st.form_submit_button("🔍 Predict Risk Level")

# Prediction
if submitted:
    input_data = pd.DataFrame(
        [[x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro, acc_magnitude]],
        columns=['x_acc','y_acc','z_acc','x_gyro','y_gyro','z_gyro','acc_magnitude']
    )
    
    prediction = model.predict(input_data)[0]
    risk_label = label_map.get(prediction, "Danger")

    st.success(f"✅ Predicted Risk Level: **{risk_label}**")
