import cv2
import face_recognition
import tkinter as tk
from PIL import Image, ImageTk

# Load images and names of people to recognize
known_image1 = face_recognition.load_image_file("known_images/known_person1.jpg")
known_image2 = face_recognition.load_image_file("known_images/known_person2.jpg")
known_image3 = face_recognition.load_image_file("known_images/known_person3.jpg")

known_face_encodings = [
    face_recognition.face_encodings(known_image1)[0],
    face_recognition.face_encodings(known_image2)[0],
    face_recognition.face_encodings(known_image3)[0]
]

known_face_names = ["Person 1", "Person 2", "Person 3"]

# Create GUI window
root = tk.Tk()
root.title("Facial Recognition")

# Create camera label
camera_label = tk.Label(root)
camera_label.pack()

# Create name label
name_label = tk.Label(root, font=("Arial", 16))
name_label.pack()

# Initialize camera
cap = cv2.VideoCapture(0)

def update_frame():
    ret, frame = cap.read()

    if ret:
        # Convert BGR image to RGB for face_recognition library
        rgb_frame = frame[:, :, ::-1]

        # Find faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare face encoding with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            # If there's a match, display the name
            if True in matches:
                name = known_face_names[matches.index(True)]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                name_label.configure(text=name)
            else:
                name_label.configure(text="Unknown")

        # Convert OpenCV image to PIL format for tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update camera label
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)

    # Schedule next update
    root.after(10, update_frame)

def no_camera_input():
    # Create black background label
    bg_label = tk.Label(root, bg="black")
    bg_label.pack(fill=tk.BOTH, expand=True)

    # Create camera icon label
    camera_icon = Image.open("camera_icon.jpg")
    camera_icon = camera_icon.resize((100, 100))
    camera_icon = ImageTk.PhotoImage(camera_icon)
    camera_icon_label = tk.Label(bg_label, image=camera_icon)
    camera_icon_label.pack(pady=50)

    # Create text label
    text_label = tk.Label(bg_label, text="No video input", font=("Arial", 24), fg="white", bg="black")
    text_label.pack(pady=50)

    # Schedule next update
    root.after(10, no_camera_input)

# Start updating the frame
if cap.isOpened():
    update_frame()
else:
    no_camera_input()

# Start GUI loop
root.mainloop()

# Release camera
cap.release()
