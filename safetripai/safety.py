import streamlit as st
from risk_detection import check_risk
from emergency import send_sos
from database import save_user

st.set_page_config(page_title="SafeTrip AI", layout="centered")

st.title("🛡 SafeTrip AI")
st.subheader("Smart Tourist Safety System")

# User Profile Section
st.header("👤 Tourist Profile")

name = st.text_input("Full Name")
blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
emergency_contact = st.text_input("Emergency Contact Number")

if st.button("Save Profile"):
    save_user(name, blood_group, emergency_contact)
    st.success("Profile Saved Successfully!")

# Risk Detection Section
st.header("📍 Location & Movement Check")

location = st.text_input("Current Location")
movement = st.selectbox("Movement Type", ["Normal", "Running", "Falling", "No Movement"])

if st.button("Check Risk"):
    result = check_risk(location, movement)
    st.warning(result)

# SOS Button
st.header("🚨 Emergency")

if st.button("SOS"):
    send_sos(name, location)
    st.error("Emergency Alert Sent!")
