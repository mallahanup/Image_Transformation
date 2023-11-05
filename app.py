import streamlit as st
from PIL import Image, ImageOps

st.title("Image Transformation App")

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    st.header("Original Image")
    st.image(image, use_column_width=True)

    transformation_type = st.selectbox("Select Transformation", ["Rotate", "Scale", "Translate", "Shear"])
    parameter = st.number_input("Enter Transformation Parameter")

    if st.button("Transform"):
        if transformation_type == "Rotate":
            transformed_image = image.rotate(parameter)
        elif transformation_type == "Scale":
            new_size = (int(image.width * parameter), int(image.height * parameter))
            transformed_image = image.resize(new_size)
        elif transformation_type == "Translate":
            transformed_image = ImageOps.offset(image, int(parameter), int(parameter))
        elif transformation_type == "Shear":
            shear_matrix = (1, parameter, 0, 0, 1, 0)
            transformed_image = image.transform(image.size, Image.AFFINE, shear_matrix)

        st.header("Transformed Image")
        st.image(transformed_image, use_column_width=True)
