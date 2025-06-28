# Deepfake Detection Using YOLOv8

This project is focused on detecting deepfake content in videos using computer vision and machine learning. Deepfakes are digitally manipulated videos where someone's face or expressions are changed using AI — and while some are harmless, others can be misleading or harmful. The goal of this project is to help identify such fake videos quickly and accurately.

We used YOLOv8 (a state-of-the-art object detection and classification model) to train a system that can classify whether a face in an image is real or fake. Here’s how it works:

- First, we collected real and fake videos from public datasets.  
- Then, we extracted frames (individual images) from these videos.  
- These images were sorted into two folders — real and fake — to prepare them for training.  
- Using YOLOv8’s image classification mode, we trained a model to learn the difference between real and fake faces based on visual patterns.  
- Finally, we tested the model on new images to check how accurately it could detect deepfakes.

This project demonstrates how deep learning can be used to fight misinformation and detect manipulated media. It can be a helpful tool for journalists, researchers, or social media platforms looking to verify visual content.
