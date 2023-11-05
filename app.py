import streamlit as st
import cv2
import numpy as np

def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, M, (cols, rows))
    return rotated_image

def scale_image(image, scale_x, scale_y):
    scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
    return scaled_image

def translate_image(image, dx, dy):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    translated_image = cv2.warpAffine(image, M, (cols, rows))
    return translated_image

def shear_image(image, shear_x, shear_y):
    shear_matrix = np.array([[1, shear_x, 0], [shear_y, 1, 0]], dtype=np.float32)
    sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))
    return sheared_image

st.title("Image Transformation App")

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

    st.header("Original Image")
    st.image(image, use_column_width=True)

    transformation_type = st.selectbox("Select Transformation", ["Rotate", "Scale", "Translate", "Shear"])
    parameter = st.number_input("Enter Transformation Parameter")

    if st.button("Transform"):
        if transformation_type == "Rotate":
            transformed_image = rotate_image(image, parameter)
        elif transformation_type == "Scale":
            transformed_image = scale_image(image, parameter, parameter)
        elif transformation_type == "Translate":
            transformed_image = translate_image(image, parameter, parameter)
        elif transformation_type == "Shear":
            transformed_image = shear_image(image, parameter, parameter)

        st.header("Transformed Image")
        st.image(transformed_image, use_column_width=True)
