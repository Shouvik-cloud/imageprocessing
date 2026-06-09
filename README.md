# Red Object Tracking using OpenCV

## Overview

This project implements a real-time red object tracking system using Python and OpenCV. The application captures live video from a webcam, detects red-colored objects in the frame, and tracks their position by drawing bounding boxes and displaying their centroid coordinates.

The project demonstrates the fundamentals of computer vision techniques such as color segmentation, contour detection, noise reduction, and object localization. It can serve as a foundation for robotics applications, gesture-based interfaces, and object-following systems.

## Features

* Real-time webcam video processing
* Detection of red-colored objects using the HSV color space
* Noise reduction using morphological operations
* Contour-based object detection
* Bounding box visualization around detected objects
* Centroid calculation and coordinate display
* Live mask preview of detected regions
* Easy exit using the ESC key

## Technologies Used

* Python 3
* OpenCV
* NumPy

## How It Works

1. The webcam continuously captures video frames.
2. Each frame is converted from BGR to HSV color space.
3. Two HSV ranges are used to detect the red color spectrum.
4. Binary masks are generated and combined.
5. Morphological operations remove noise from the mask.
6. Contours are extracted from the processed mask.
7. Significant contours are identified based on their area.
8. Bounding boxes and centroid coordinates are drawn on the detected object.
9. The processed video and mask are displayed in separate windows.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

Install the required dependencies:

```bash
pip install opencv-python numpy
```

## Usage

Run the application using:

```bash
python main.py
```

### Controls

* **ESC** : Exit the application

## Project Applications

* Object-following robots
* Human-computer interaction systems
* Gesture recognition prototypes
* Educational computer vision projects
* Color-based sorting and tracking systems

## Future Improvements

* Track only the largest object.
* Support detection of multiple colors.
* Integrate with Arduino for robot control.
* Display object trajectory.
* Improve robustness under varying lighting conditions.

## Output

The application displays:

* A live webcam feed with a green bounding box around the detected red object.
* A blue dot representing the object's centroid.
* Real-time X and Y coordinates.
* A separate mask window highlighting detected red regions.

## License

This project is open-source and available for educational and learning purposes.
