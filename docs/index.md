---
layout: default
---

# Overview
Dominant colors in an image are detected according to their Hue, Saturation and Value of intensity. This is extended to videos by applying the same to each frame. For video purpose, I've used webcam. This project is done using OpenCV, a package for Image Analysis in Python.

## Requirements
Install Python3.x, and then install OpenCV by following [this](https://www.codingforentrepreneurs.com/blog/install-opencv-3-for-python-on-mac/) page. That page is escpecially the installation instructions for mac users.

## Concept
*   First, HSV format is extracted from tthe original image/frame.
```python
hsv_version = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

*   We make the filtering using single mask layer that we create. Resultant will be the `bitwise_and` of the mask and the original frame. Let's see the mask later, I've the stub below to explain.
```python
res = cv2.bitwise_and(frame, frame, mask=mask)
```

*   Actually, the mask is not yet defined. Let's see what the mask actually is. In OpenCV, Hue ranges from 0 to 180, Saturation tanges from 0 to 255 aand Value of Intensity ranges from 0 to 255. Below showed picture describes the variation.
![hsv](hsv.png)


## Results
