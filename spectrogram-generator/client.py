import requests
import json

# Place your .wav files in the content dir
# Create it if not already present
audio_path = 'content/sample.wav'

# URL to which the file will be sent
api_endpoint = 'http://127.0.0.1:3000/upload'

with open(audio_path, 'rb') as audio_file:
    # Read the file as raw bytes
    audio_bytes = audio_file.read()

payload = {
    'audio_data': list(audio_bytes)  # Convert bytes to a list of integers
}

response = requests.post(api_endpoint, json=payload)  # Send the request

print("Server response time (excluding the response download time): {}".format(
    response.elapsed.total_seconds()))

# Check if the request was successful
if response.status_code == 200:
    # Save the response as an image at 'content/spectrogram_magnitudes.txt'
    with open("content/spectrogram_magnitudes.txt", "w") as file:
        content_json = json.loads(response.content)
        print(content_json["audio_data"], file=file)
else:
    print(f"Failed to upload image. Status code: {response.status_code}")
    print("Response:", response.text)
