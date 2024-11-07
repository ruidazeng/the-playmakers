# NFL Position Classification Through YOLO

![image](https://github.com/user-attachments/assets/fdcc2da0-96f8-4be9-ba68-f381dbbcbf30)
![image](https://github.com/user-attachments/assets/426cc15a-83cb-4eec-a6ab-a2581b76562f)



## Real-Time NFL Player Position Classification with YOLOv8

**Playmakers** is a machine learning project aimed at real-time classification of NFL player positions using the YOLOv8 deep learning model. This end-to-end application leverages custom data and cutting-edge object detection techniques to classify positions on the football field before each play. With applications in sports analytics, this project advances real-time classification and contextual object detection.

## Overview

Playmakers is designed to classify NFL player positions based on pre-snap formations, a challenging task due to the homogeneity of players' appearances. By using YOLOv8 for its speed and precision, this project showcases the potential of contextual object detection in sports analytics.

The system combines:
- **Deep Learning** for NFL player position detection.
- **Custom Dataset** built from NFL game footage.
- **YOLOv8 Model** optimized for speed and context-sensitive classification.

## Features

- **End-to-End Object Detection Pipeline**: From data preprocessing to real-time inference, all components are production-ready.
- **Custom Data Handling**: Processed NFL footage with over 500 annotated images for training.
- **Scalable Architecture**: Optimized for real-time predictions, supporting analysis of entire game footage sequences.

## Architecture

Playmakers consists of three main components:
1. **Custom Data Pipeline**: A dataset of NFL formations, processed and labeled to capture player positions accurately.
2. **YOLOv8-Based Detection Model**: Trained on labeled NFL footage to identify player positions in real-time.
3. **Visualization Module**: Displays bounding boxes and confidence scores for detected player positions.

## Installation and Setup

### Prerequisites

- Python 3.x
- OpenCV
- Roboflow account for data management

### Usage

Once setup is complete, run the application locally to process NFL footage and visualize detected player positions. Adjust model parameters for optimal performance and explore different confidence thresholds for various classification needs.

## Evaluation

The model was evaluated on:
- **Detection Accuracy**: Achieved mean accuracy precision (mAP) of 0.759 at a confidence threshold of 0.5.
- **Performance on Diverse Positions**: Strong results for wide receivers and cornerbacks, with room for improvement for more densely packed formations.
- **Confusion Analysis**: Visualized performance using confusion matrices and precision-recall curves.

## Future Directions

Potential improvements include:
- Expanding the dataset for diverse formations and player setups.
- Experimenting with alternative models like DETR or Swin Transformer for accuracy improvements in dense formations.
- Implementing tracking features for in-play analysis.


## Contributors

John Michael Slezak

Atif Khan

Chenhao Lu

Ruida Zeng

### For questions or suggestions, please reach out via GitHub Issues or email. 
