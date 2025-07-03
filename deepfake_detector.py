import ultralytics as yolo
import requests
import cv2
import sys

# Load the YOLOv8 model
model = yolo.YOLO('yolov8s.pt')

# Set up the Roboflow API credentials
api_key = 'rf_wENmY3rw2uc34e81qibdVJtQfti1'  # Replace this with your actual API key
endpoint = 'https://api.roboflow.com/v1/detect'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

def detect_deepfake(image_path, video_path):
    # Load the image and video using OpenCV
    image = cv2.imread(image_path)
    video = cv2.VideoCapture(video_path)

    # Pre-process the image
    image_resized = cv2.resize(image, (640, 640))  # Resize to model input size

    # Detect deep fakes using YOLOv8
    results = model(image_resized)  # run YOLO on image

    # Get the detection results
    deepfake_score = 0
    if results.boxes is not None and len(results.boxes) > 0:
        deepfake_score = max([box.conf for box in results.boxes])  # Use max confidence as score
    else:
        print("No detections made in the image.")

    # Send the request to Roboflow API (for additional deepfake detection)
    payload = {
        'image': image_path,
        'video': video_path
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    
    # Check if the response is successful
    if response.status_code == 200:
        roboflow_score = response.json().get('score', 0)  # Get score from response
    else:
        print(f"Roboflow API error: {response.status_code} - {response.text}")
        roboflow_score = 0

    # Combine the YOLOv8 and Roboflow scores
    final_score = (deepfake_score + roboflow_score) / 2 if roboflow_score else deepfake_score

    return final_score

def main():
    # Get the image and video paths from command line arguments
    image_path = sys.argv[1]
    video_path = sys.argv[2]

    # Detect deep fakes
    score = detect_deepfake(image_path, video_path)

    # Print the deep fake detection score
    print(f'Deep fake score: {score:.2f}')

if __name__ == '__main__':
    main()
