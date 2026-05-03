import cv2
import os

# Ask for student name
student_name = input("Enter Student Name: ")

# Create student folder path
dataset_path = os.path.join("dataset", student_name)

# Make folder if it doesn't exist
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Start webcam
cam = cv2.VideoCapture(0)

# Load face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0

print("Look at the camera... Capturing face images.")

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to access webcam")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        count += 1

        # Crop face
        face = frame[y:y+h, x:x+w]

        # Save image
        file_name = os.path.join(dataset_path, f"{count}.jpg")
        cv2.imwrite(file_name, face)

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Show count
        cv2.putText(
            frame,
            f"Images Captured: {count}/50",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Registration", frame)

    # Stop when Enter key pressed OR 50 images collected
    if cv2.waitKey(1) == 13 or count >= 50:
        break

# Release resources
cam.release()
cv2.destroyAllWindows()

print(f"Face registration complete for {student_name}")
