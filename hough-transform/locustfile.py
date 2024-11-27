from locust import HttpUser, task, between
import os
import json

class ImageUploadUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between tasks

    @task
    def upload_image(self):
        # Path to the image file you want to upload
        image_path = "content/request.png"
        
        # Check if the file exists
        if not os.path.exists(image_path):
            print(f"File {image_path} does not exist.")
            return
        
        # Read the image file as bytes
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        
        payload = {
            'image_data': list(image_data)
        }

        payload = json.dumps(payload)

        # Send a POST request with the image data
        self.client.post("/upload", data=payload, headers={"Content-Type": "application/json"})

# To run the Locust test, use the command:
# locust -f locustfile.py --host=http://127.0.0.1:3000

