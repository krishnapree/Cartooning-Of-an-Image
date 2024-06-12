from flask import Flask, request, render_template, send_file
import os
import cv2
import numpy as np
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def cartoonize_image(images):
    
    upscale_images = []
    for img in images:
        upscaled_img = cv2.pyrUp(img)  
        upscale_images.append(upscaled_img)

    grayscale_images = []
    for img in upscale_images:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
        grayscale_images.append(gray_img)

    blurred_images = []
    for img in grayscale_images:
        blurred_img = cv2.medianBlur(img, 7)  
        blurred_images.append(blurred_img)

    edge_images = []
    for img in blurred_images:
        edge_img = cv2.adaptiveThreshold(
            img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 2)
        edge_images.append(edge_img)

    rgb_edges = []
    for img in edge_images:
        rgb_edge_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) 
        rgb_edges.append(rgb_edge_img)

    cartoonized_images = []
    for original_img, edge_img in zip(upscale_images, rgb_edges):
        cartoon_img = cv2.bitwise_and(original_img, edge_img)  
        cartoonized_images.append(cartoon_img)

    return cartoonized_images


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        # Read uploaded image
        img = cv2.imread(file_path)
        # Process image to create cartoon-like effect
        cartoon_images = cartoonize_image([img])
        # Save cartoon image temporarily
        cartoon_img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cartoon.jpg')
        cv2.imwrite(cartoon_img_path, cartoon_images[0])

        # Provide the cartoon image as a downloadable link
        return send_file(cartoon_img_path, mimetype='image/jpeg')

    return "Analysis failed"

if __name__ == "__main__":
    app.run(debug=True)