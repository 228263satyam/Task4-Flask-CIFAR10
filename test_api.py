import requests
import os

API_URL = "http://127.0.0.1:5000"


# ----------------------------------------
# Test 1: Home Endpoint
# ----------------------------------------

print("\n========== TEST 1: HOME ENDPOINT ==========")

response = requests.get(API_URL + "/")

print("Status Code:", response.status_code)
print("Response:", response.json())


# ----------------------------------------
# Test 2: Health Endpoint
# ----------------------------------------

print("\n========== TEST 2: HEALTH ENDPOINT ==========")

response = requests.get(API_URL + "/health")

print("Status Code:", response.status_code)
print("Response:", response.json())


# ----------------------------------------
# Test 3: Error Handling
# ----------------------------------------

print("\n========== TEST 3: ERROR HANDLING ==========")

response = requests.post(API_URL + "/predict")

print("Status Code:", response.status_code)
print("Response:", response.json())


# ----------------------------------------
# Test 4: Image Prediction
# ----------------------------------------

print("\n========== TEST 4: IMAGE PREDICTION ==========")

IMAGE_PATH = "test_image.png"

if not os.path.exists(IMAGE_PATH):

    print("ERROR: test_image.png not found.")
    print("Please place a test image in the project folder.")

else:

    with open(IMAGE_PATH, "rb") as image:

        response = requests.post(
            API_URL + "/predict",
            files={
                "image": (
                    "test_image.png",
                    image,
                    "image/png"
                )
            }
        )

    print("Status Code:", response.status_code)
    print("Prediction Response:")
    print(response.json())