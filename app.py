import streamlit as st
import pandas as pd
import os

# Page title
st.set_page_config(page_title="Face Attendance System", layout="wide")

st.title("Face Detection Attendance System")

# Sidebar menu
menu = ["Home", "Face Registration", "Live Attendance", "Attendance Report"]
choice = st.sidebar.selectbox("Menu", menu)

# HOME PAGE
if choice == "Home":
    st.subheader("Welcome")
    st.write("This system registers students, marks attendance, and shows reports.")

# FACE REGISTRATION PAGE
elif choice == "Face Registration":
    st.subheader("Face Registration")
    st.write("Run register_face.py separately to collect student images.")

# LIVE ATTENDANCE PAGE
elif choice == "Live Attendance":
    st.subheader("Live Attendance")
    st.write("Live webcam attendance system will be added here.")

# ATTENDANCE REPORT PAGE
elif choice == "Attendance Report":
    st.subheader("Attendance Report")

    if os.path.exists("attendance.csv"):
        df = pd.read_csv("attendance.csv")
        st.dataframe(df)
    else:
        st.warning("No attendance records found.")
