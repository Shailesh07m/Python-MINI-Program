
#this all chat gpt because i didn't knew image shoing in python
# Import the requests library
# requests allows us to send HTTP requests to APIs
import requests


# Step 1: API endpoint that returns random dog image URL in JSON
api_url = "https://dog.ceo/api/breeds/image/random"


# Step 2: Send GET request to Dog API
# GET means we are retrieving data
response = requests.get(api_url, timeout=5)


# Step 3: Convert response JSON into Python dictionary
# .json() parses JSON text into Python dict
data = response.json()


# Step 4: Extract image URL from dictionary
# data is a dict
# "message" key contains image URL
image_url = data["message"]


# Step 5: Send another GET request to download actual image
# This time we are not getting JSON
# We are getting binary image data
image_response = requests.get(image_url, timeout=5)


# Step 6: Open a file in binary write mode
# "wb" means:
# w = write mode
# b = binary mode (important for images)
with open("dog_image.jpg", "wb") as file:

    # Step 7: Write raw image bytes into file
    # image_response.content contains binary data
    file.write(image_response.content)


# Step 8: Print confirmation
print("Image downloaded and saved as dog_image.jpg")
