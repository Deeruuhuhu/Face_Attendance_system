# Face_Attendance_system
Issue: Face Detection Attendance System not fully functional due to missing camera input
📌 Problem Summary

The Streamlit-based Face Detection Attendance System runs successfully and the UI loads without errors, but the core functionality (live face detection and attendance marking) cannot be tested or executed because the system has no working camera input.

⚙️ Current Behavior
Streamlit application launches correctly
Navigation between pages (Home, Face Registration, Live Attendance, Attendance Report) works
Attendance report section displays CSV data if available
Face recognition training script exists but cannot be fully validated
Live Attendance module does not function as intended due to lack of webcam access
🚫 Root Cause
No working webcam device available on the system
Therefore, real-time face capture for dataset creation and recognition is not possible
Model training and prediction cannot be properly validated without input images or video stream
