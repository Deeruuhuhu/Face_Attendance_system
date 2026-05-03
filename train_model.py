import cv2
import os
import numpy as np

dataset_path = "dataset"

# Face detector
detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = []
labels = []
label_map = {}

current_id = 0

print("Training started...")

# Loop through student folders
for student_name in os.listdir(dataset_path):
    student_folder = os.path.join(dataset_path, student_name)

    if not os.path.isdir(student_folder):
        continue

    label_map[current_id] = student_name

    for image_name in os.listdir(student_folder):
        image_path = os.path.join(student_folder, image_name)

        img = cv2.imread(image_path)
        
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected_faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in detected_faces:
            faces.append(gray[y:y+h, x:x+w])
            labels.append(current_id)

    current_id += 1

# Train LBPH model
recognizer = cv2.face.LBPHFaceRecognizer_create()

if len(faces) > 0:
    recognizer.train(faces, np.array(labels))

    if not os.path.exists("trained_model"):
        os.makedirs("trained_model")

    recognizer.save("trained_model/trainer.yml")

    # Save label map
    with open("trained_model/labels.txt", "w") as f:
        for id, name in label_map.items():
            f.write(f"{id},{name}\n")

    print("Training complete!")
    print(f"Total students trained: {len(label_map)}")

else:
    print("No valid face data found in dataset.")
