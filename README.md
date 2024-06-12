Certainly! Here is a README file description for your project to upload on GitHub:

---

# Cartoonize Image Web Application

This project is a web application that allows users to upload an image and apply a cartoon-like effect to it using OpenCV. The application is built with Flask, a lightweight WSGI web application framework for Python.

## Features

- Upload an image file (supports various image formats).
- Apply a cartoon-like effect to the uploaded image.
- Download the processed cartoonized image.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/krishnapree/Cartooning-Of-an-Image.git
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your web browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Dependencies

- Flask
- OpenCV (opencv-python-headless)
- NumPy

## Project Structure

```
cartoonize-image/
│
├── app.py               # Main Flask application
├── requirements.txt     # List of dependencies
├── templates/
│   └── index.html       # HTML template for the web interface
└── uploads/             # Directory to store uploaded and processed images
```

## Code Overview

### Flask Application (`app.py`)

The Flask application is configured to handle file uploads, process the images, and return the cartoonized images.

- **Routes**:
  - `/` : Renders the index page with the upload form.
  - `/upload` : Handles the image upload, processes the image, and returns the cartoonized image.

- **Image Processing**:
  - **Upscaling**: Increases the size of the image using `cv2.pyrUp`.
  - **Grayscale Conversion**: Converts the image to grayscale.
  - **Blurring**: Applies a median blur to the grayscale image.
  - **Edge Detection**: Detects edges using adaptive thresholding.
  - **Combining Edges with Original Image**: Combines the edges with the original image to create a cartoon effect.

### HTML Template (`index.html`)

The HTML template provides a simple interface for users to upload an image file.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cartooning Of an Image</title>
  </head>
  <body>
    <h1>Upload an image to cartoonize</h1>
    <form method="post" enctype="multipart/form-data" action="/upload">
      <input type="file" name="file" accept="image/*" required />
      <input type="submit" value="Upload" />
    </form>
  </body>
</html>
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This README provides a comprehensive overview of the project, instructions for setting it up, and an explanation of its structure and functionality. Adjust the repository URL and any other specifics to match your actual project setup.
