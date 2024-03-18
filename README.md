
# Face Swapping Tool
The Face Swapping Tool is a Streamlit-based web application that allows users to upload two images of faces and perform face swapping between them. The tool utilizes image processing techniques, facial landmark detection, and convex hull algorithms to seamlessly swap faces while maintaining natural appearance.


## Key Features

- Image Upload: Allows users to upload two images of faces (base image and mask image) in common formats such as JPG, JPEG, and PNG.

- Image Cropping: Provides a built-in cropping tool that enables users to select rectangular regions over the uploaded images to crop the faces accurately.

- Orientation Correction: Automatically corrects the orientation of uploaded images based on EXIF metadata to ensure consistent processing.

- Facial Landmark Detection: Utilizes the dlib library for facial landmark detection, which accurately identifies key points on the faces, such as eyes, nose, mouth, and chin.

- Triangulation: Performs Delaunay triangulation on the detected facial landmarks to divide the faces into corresponding triangles for accurate mapping.

- Face Swapping: Implements face swapping by warping and blending the triangles from one face onto the other, resulting in a seamless transition between the faces.

- Seamless Cloning: Utilizes the OpenCV seamlessClone function to blend the swapped face into the target face seamlessly, ensuring a natural appearance.

- Error Handling: Provides error handling to handle exceptions during image processing and swapping, ensuring a smooth user experience and informative error messages.
## Libraries Used:

- Streamlit: Used for building interactive web applications with Python, providing a user-friendly interface for uploading images and displaying results.

- PIL (Python Imaging Library): Utilized for image processing tasks such as resizing, orientation correction, and saving images.

- OpenCV (cv2): Employed for advanced image processing functionalities, including facial landmark detection, image manipulation, and seamless cloning.

- NumPy: Used for numerical computation and array manipulation, facilitating various mathematical operations during image processing.

- dlib: Integrated for face detection and facial landmark estimation, offering robust algorithms and pre-trained models for accurate facial feature detection.

- Requests: Used for fetching images from the internet, although not explicitly mentioned in the provided code.

- Shutil: Employed for file and directory operations, including clearing folders to ensure a clean environment for each execution of the application.
## Project Components:
#### app.py:
- This Python script serves as the main application file for the Streamlit-based web application.
- It imports necessary libraries such as Streamlit, PIL (Python Imaging Library), and OpenCV (cv2).
- The create_folder_if_not_exist function is defined to create folders for storing uploaded and cropped images if they don't exist.
- The fix_orientation function corrects the orientation of images based on EXIF metadata.
- The clear_folder function clears the contents of the specified folder by removing all files and subdirectories.
- The main function is the entry point of the application. It sets up the Streamlit sidebar for image upload, handles image processing, and displays the results.

#### swap_face.py:
- This Python script contains functions related to facial landmark detection, triangulation, and face swapping.
- It imports libraries such as cv2 (OpenCV), numpy (numerical computation), and dlib (face detection and landmark estimation).
- The extract_index_nparray function extracts the index from a NumPy array.
- The check_and_convert_orientation_conv_gray function checks and converts the orientation of the image to grayscale.
- The swap function performs the face swapping process using facial landmarks and convex hull algorithms.
## Installation

requirements.txt

run this command in terminal
```bash
  pip install -r requirements.txt
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/phinglaspure123/Face-Swap-App.git
```

Go to the project directory

```bash
  "Face Swap App"
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```

## Deployment

To deploy this project run

  [@Heroku](https://face-swap-app-2de2a4bd6261.herokuapp.com/)

## Authors

- [@phinglaspure123](https://github.com/phinglaspure123)

