import requests
import json

# Place your .png files in the content dir
# Create it if not already present
image_path = 'content/request.png'

# URL to which the image will be sent
api_endpoint = 'http://127.0.0.1:3000/upload'

with open(image_path, 'rb') as image_file:
    # Read the image file as raw bytes
    image_bytes = image_file.read()

payload = {
    'image_data': list(image_bytes)  # Convert bytes to a list of integers
}

response = requests.post(api_endpoint, json=payload)  # Send the request

print("Server response time (excluding the response download time): {}".format(
    response.elapsed.total_seconds()))

# Check if the request was successful
if response.status_code == 200:
    # Save the response as an image at 'content/response.png'
    with open("content/response.png", "wb") as file:
        # content_json = json.loads(response.content)
        # print(content_json["image_data"], file=file)
        file.write(response.content)
else:
    print(f"Failed to upload image. Status code: {response.status_code}")
    print("Response:", response.text)
