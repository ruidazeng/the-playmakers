# The Playmakers

**John Michael Slezak, Atif Khan, Chenhao Lu, Ruida Zeng**  
**Brown University CS 1430 Computer Vision Final Project**

**TA Mentor:** Joel Manasseh  
**Professor:** Srinath Sridhar  

## NFL Position Classification Through YOLO

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

The model's performance was assessed using the following metrics, based on detailed visualizations:

- **F1-Confidence Curve**: The F1 score peaked at 0.62 at a confidence threshold of 0.229 across all classes, reflecting an effective balance between precision and recall at this threshold. The curve shows that Wide Receiver and Safety positions maintain high F1 scores across varying confidence levels, while positions like Fullback and Tight End experience more fluctuation, indicating variable performance across different positions.  
  <img src="https://github.com/user-attachments/assets/ec6ac025-fd98-490b-a9ee-4e5ae1c00b3c" width="500"/>

- **Precision-Recall Curve**: Achieved a mean average precision (mAP) of 0.759 at an IoU threshold of 0.5, with class-specific precision scores such as 0.942 for Wide Receiver, 0.885 for Corner Back, and 0.879 for Safety. This curve highlights that certain positions, particularly Wide Receiver and Safety, have high precision and recall, while others, like Fullback (0.454), exhibit more challenges in maintaining consistent accuracy.  
  <img src="https://github.com/user-attachments/assets/1d09e654-94bc-4795-917c-616135eb0e9d" width="500"/>

- **Confusion Matrix**: The model displays strong classification accuracy for positions like Wide Receiver (234 true positives) and Corner Back (200 true positives), but shows confusion among some positions, such as misclassifying Linebackers and Safeties. Background interference and similar player formations contribute to some of the confusion, particularly for positions like Running Back and Quarterback.  
  <img src="https://github.com/user-attachments/assets/7b4ce9ac-fb60-48d3-a80e-9bae13c234e9" width="500"/>


These metrics collectively highlight the model's strengths in detecting key positions on the field, with room for improvement in differentiating more ambiguous positions under varying formations.

## Future Directions

Potential improvements include:
- Expanding the dataset for diverse formations and player setups.
- Experimenting with alternative models like DETR or Swin Transformer for accuracy improvements in dense formations.
- Implementing tracking features for in-play analysis.

### For questions or suggestions, please reach out via GitHub Issues or email. 
