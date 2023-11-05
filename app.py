import streamlit as st
import cv2
numpy as np
from image_transformation import *

st.title("Image Transformation App")

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

    # Display the original image
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

        # Display the transformed image
        st.header("Transformed Image")
        st.image(transformed_image, use_column_width=True)
