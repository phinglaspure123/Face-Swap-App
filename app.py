import os
import streamlit as st
from PIL import Image, ExifTags
from streamlit_cropper import st_cropper
from swap_face import check_and_convert_orientation_conv_gray, swap
import shutil

UPLOADS_FOLDER = "uploads"
CROPPED_FOLDER = "cropped"

st.markdown(
    """
<style>
    div[data-testid="stSidebarUserContent"] {
        padding: 2rem 1.5rem;
    }
    div[data-testid="stAppViewBlockContainer"]{
        max-width: 66rem;
    }
</style>
""",
    unsafe_allow_html=True,
)


def create_folder_if_not_exist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def fix_orientation(image):
    try:
        # Check if image has orientation info in EXIF data
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = dict(image._getexif().items())

        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # Image has no EXIF metadata or no orientation info
        pass

    max_size = (300, 300)
    image.thumbnail(max_size)
    return image

def clear_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)



def main():
    
    clear_folder(UPLOADS_FOLDER)
    clear_folder(CROPPED_FOLDER)
    
    create_folder_if_not_exist(UPLOADS_FOLDER)
    create_folder_if_not_exist(CROPPED_FOLDER)

    st.sidebar.title("Upload Images")
    uploaded_image1 = st.sidebar.file_uploader("Upload Base Image", type=["jpg", "jpeg", "png"])
    uploaded_image2 = st.sidebar.file_uploader("Upload Mask Image", type=["jpg", "jpeg", "png"])

    if uploaded_image1 and uploaded_image2:
        # Save uploaded images to uploads folder
        image1_path = os.path.join(UPLOADS_FOLDER, uploaded_image1.name)
        image2_path = os.path.join(UPLOADS_FOLDER, uploaded_image2.name)
        with open(image1_path, "wb") as f1, open(image2_path, "wb") as f2:
            f1.write(uploaded_image1.read())
            f2.write(uploaded_image2.read())

        # Convert uploaded images to PIL Image
        pil_image1 = Image.open(image1_path)
        pil_image2 = Image.open(image2_path)

        # Fix image orientations if needed
        pil_image1 = fix_orientation(pil_image1)
        pil_image2 = fix_orientation(pil_image2)

        st.title("Face Swapping Tool")
        col1, col2,col3 = st.columns(3)
        with col1:
            st.text("Cropped Base Image:")
            cropped_image1 = st_cropper(pil_image1)
            if cropped_image1:
                # Save the cropped image
                cropped_image1_path = os.path.join(CROPPED_FOLDER, "cropped_image1.jpg")
                cropped_image1.save(cropped_image1_path)
        with col2:
            st.text("Cropped Mask Image:")
            cropped_image2 = st_cropper(pil_image2)
            if cropped_image2:
                # Save the cropped image
                cropped_image2_path = os.path.join(CROPPED_FOLDER, "cropped_image2.jpg")
                cropped_image2.save(cropped_image2_path)
        with col3:
            st.text("Output:")
            if 'cropped_image1_path' in locals() and 'cropped_image2_path' in locals():
                try:
                    # Process and convert the images
                    x = check_and_convert_orientation_conv_gray(cropped_image1_path)
                    y = check_and_convert_orientation_conv_gray(cropped_image2_path)
                    st.image(swap(x, y))
                except Exception as e:
                    st.error(f"Selection wrong please selection face (head to chin)")

    


if __name__ == "__main__":
    main()
