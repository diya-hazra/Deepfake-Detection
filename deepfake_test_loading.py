import cv2

def test_loading(image_path, video_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading image: {image_path}")
    else:
        print(f"Image loaded successfully: {image.shape}")

    # Load the video
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error loading video: {video_path}")
    else:
        print("Video loaded successfully.")

        # Read one frame to ensure it's working
        ret, frame = video.read()
        if ret:
            print(f"First frame read successfully: {frame.shape}")
        else:
            print("Failed to read the first frame.")

    video.release()

# Replace with your actual paths
test_loading("C:\\Users\\Diya Hazra\\Desktop\\Deepfake Detector\\cat.jpeg", "C:\\Users\\Diya Hazra\\Desktop\\Deepfake Detector\\dog3.jpeg")
