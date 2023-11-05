from flask import Flask, request, render_template, send_from_directory
import cv2
import numpy as np
from image_transformation import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform', methods=['POST'])
def transform():
    if 'image' in request.files:
        image_file = request.files['image']
        transformation_type = request.form['transformation']
        parameter = float(request.form['parameter'])

        # Load the uploaded image into a NumPy array using OpenCV
        image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        cv2.imwrite('static/original_image.jpg', image)

        if transformation_type == 'rotate':
            transformed_image = rotate_image(image, parameter)
        elif transformation_type == 'scale':
            transformed_image = scale_image(image, parameter, parameter)
        elif transformation_type == 'translate':
            transformed_image = translate_image(image, parameter, parameter)
        elif transformation_type == 'shear':
            transformed_image = shear_image(image, parameter, parameter)

        # Save the transformed image using OpenCV
        cv2.imwrite('static/transformed_image.jpg', transformed_image)

        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
