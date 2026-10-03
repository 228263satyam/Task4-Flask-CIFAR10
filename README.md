# Task 4: Flask API for Deep Learning Model

## CIFAR-10 Image Classification using CNN and Flask REST API

This project is developed as part of **Task 4: Developing a Flask API for Deep Learning Models**.

The project demonstrates how a trained deep learning model can be exposed through a REST API using the Flask framework. A Convolutional Neural Network (CNN) was trained on the **CIFAR-10 dataset** using TensorFlow/Keras in Google Colab. The trained model was then saved and integrated into a Flask application developed and tested in Visual Studio Code.

---

## Project Objective

The objective of this project is to:

- Train a deep learning image-classification model using CIFAR-10.
- Evaluate the trained model.
- Save the trained model.
- Load the trained model into a Flask application.
- Create REST API endpoints for model interaction.
- Accept image input through an API request.
- Return prediction results in JSON format.
- Implement input validation and error handling.
- Test the API using Python requests.

---

## Dataset

### CIFAR-10

CIFAR-10 is an image classification dataset containing 60,000 color images divided into 10 classes.

The classes are:

1. Airplane
2. Automobile
3. Bird
4. Cat
5. Deer
6. Dog
7. Frog
8. Horse
9. Ship
10. Truck

The dataset contains:

- 50,000 training images
- 10,000 testing images
- Image size: 32 × 32 pixels
- 3 color channels (RGB)
- 10 output classes

---

## Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- NumPy
- Pillow
- Requests
- Google Colab
- Visual Studio Code
- GitHub

---

## Machine Learning Workflow

The model development process follows these steps:

```text
CIFAR-10 Dataset
       |
       v
Data Preprocessing
       |
       v
CNN Model
       |
       v
Model Training
       |
       v
Model Evaluation
       |
       v
Saved Model
cifar10_model.keras
       |
       v
Flask REST API
       |
       v
Image Prediction
       |
       v
JSON Response
