from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

MODEL_PATH = "cifar10_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "CIFAR-10 Deep Learning Flask API",
        "status": "running",
        "model": "CNN",
        "dataset": "CIFAR-10"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "model_loaded": True
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        if "image" not in request.files:
            return jsonify({
                "success": False,
                "error": "No image file provided."
            }), 400

        file = request.files["image"]

        if file.filename == "":
            return jsonify({
                "success": False,
                "error": "No image selected."
            }), 400

        image = Image.open(file).convert("RGB")

        image = image.resize((32, 32))

        image_array = np.array(image).astype("float32") / 255.0

        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(
            image_array,
            verbose=0
        )[0]

        predicted_index = int(np.argmax(prediction))

        predicted_class = CLASS_NAMES[predicted_index]

        confidence = float(prediction[predicted_index])

        probabilities = {
            CLASS_NAMES[i]: round(float(prediction[i]), 4)
            for i in range(len(CLASS_NAMES))
        }

        return jsonify({
            "success": True,
            "prediction": predicted_class,
            "confidence": round(confidence, 4),
            "probabilities": probabilities
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )