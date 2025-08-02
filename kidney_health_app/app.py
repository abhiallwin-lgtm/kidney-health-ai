# app.py
import streamlit as st
from utils.extract_data import extract_from_pdf, extract_from_image
from utils.predict import predict_ckd
from utils.chatbot import kidney_chatbot
from utils.hospital_map import show_nearby_hospitals

st.set_page_config(page_title="Kidney Disease AI", layout="wide")

st.title("🩺 Kidney Disease Prediction AI")

# Sidebar menu
option = st.sidebar.selectbox("Choose an option", [
    "Home", "Upload Report", "Prediction Result", "Health Graph", "Nearby Hospitals", "Consult Doctor", "Ask AI Bot"
])

# --- Home ---
if option == "Home":
    st.markdown("### Welcome to Kidney Health AI")
    st.image("https://images.unsplash.com/photo-1588776814546-ec7e195f0a9b", use_column_width=True)
    st.write("""
    This app helps detect **early-stage Chronic Kidney Disease (CKD)** from lab reports. 
    It also shows predictions, health advice, hospital maps, and lets you talk to an AI chatbot.
    """)

# --- Upload Report ---
elif option == "Upload Report":
    st.subheader("Upload Blood Report (PDF or Image)")

    uploaded_file = st.file_uploader("Upload here", type=['pdf', 'png', 'jpg', 'jpeg'])

    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            extracted_data = extract_from_pdf(uploaded_file)
        else:
            extracted_data = extract_from_image(uploaded_file)

        st.session_state['input_data'] = extracted_data
        st.success("✅ Data extracted successfully. Proceed to 'Prediction Result'.")

# --- Prediction Result ---
elif option == "Prediction Result":
    st.subheader("Prediction Based on Report")

    if 'input_data' in st.session_state:
        result, confidence = predict_ckd(st.session_state['input_data'])
        st.write(f"**Prediction:** `{result}`")
        st.write(f"**Confidence:** `{confidence:.2f}%`")
    else:
        st.warning("Please upload a report first.")

# --- Health Graph ---
elif option == "Health Graph":
    st.subheader("Health Indicator Graph")
    st.line_chart({"Creatinine": [0.8, 1.2, 1.4, 2.0]})  # Placeholder

# --- Nearby Hospitals ---
elif option == "Nearby Hospitals":
    st.subheader("Hospitals Near You")
    show_nearby_hospitals()

# --- Consult Doctor ---
elif option == "Consult Doctor":
    st.subheader("Online Doctor Consultancy")
    st.markdown("""
    **Dr. Anjali Verma (MBBS, MD Nephrology)**  
    🌟 Rating: 4.9/5 (342 reviews)  
    💬 Languages: English, Hindi  
    [Book a Chat ₹199](#)
    """)

# --- Ask AI Bot ---
elif option == "Ask AI Bot":
    st.subheader("AI Chatbot - Kidney Health Advisor")
    user_q = st.text_input("Ask something about kidney health:")
    if user_q:
        answer = kidney_chatbot(user_q)
        st.write("🤖", answer)
