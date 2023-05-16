# Facial Recognition Python Script

This Python script uses OpenCV, face recognition, and tkinter to create a GUI that can recognize faces in real-time using a camera. The script loads images of known people and their names, and displays the name of the recognized person in a box around their face.

**Prerequisites**
```
Before running the script, make sure you have the following libraries installed:

- OpenCV
- face recognition
- tkinter
- PIL
```
# **You can install these libraries using pip:**

```
pip install opencv-python face-recognition tkinter pillow
```
# Usage

**Clone the repository to your local machine:**
```
git clone https://github.com/xenon-droid/PythonFacialRecon.git
Navigate to the cloned repository:

cd repository

Open the script file in your preferred text editor:

nano facial_recognition.py

Modify the script to load images of the people you want to recognize and their names. You can do this by replacing the known_image1.jpg, known_image2.jpg, known_image3.jpg files with your own images, and updating the known_face_encodings and known_face_names lists accordingly.

Save the changes to the script file.
```
# Run the script:

```
python facial_recognition.py
The GUI window should appear, displaying the camera feed and the name of the recognized person in a box around their face.
```
# Contributing
**If you find any bugs or issues with the script, feel free to open a GitHub issue or submit a pull request.**

**License**
**This project is licensed under the MIT License. See the LICENSE file for details.**
