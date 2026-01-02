# Iris Detection and Tracking Project

This project implements an eye-tracking system using deep learning. It captures images, processes them, and trains a neural network to predict the coordinates of the iris (pupil center) within the eye.

## Project Structure

*   `DataCollection.ipynb`: Notebook for capturing images from a webcam, organizing data, and performing data augmentation to create a robust dataset.
*   `IrisEstimation.ipynb`: Notebook for building, training, and evaluating the Convolutional Neural Network (CNN) model. It also includes a real-time detection demo.
*   `aug_data/`: Directory where augmented training, testing, and validation data is stored (created by `DataCollection.ipynb`).
*   `data/`: Directory for raw captured images and labels.

## Prerequisites

*   Python 3.7+
*   TensorFlow
*   OpenCV
*   Matplotlib
*   Albumentations
*   LabelMe (for annotating images)

## Installation

Install the required dependencies:

```bash
pip install tensorflow opencv-python matplotlib albumentations labelme
```

## Usage Workflow

1.  **Data Collection & Annotation**:
    *   Run `DataCollection.ipynb` to capture images of your eyes using your webcam.
    *   Annotate the images using `LabelMe`. Create a polygon or point for the eye centers.
    *   Ensure the labels are saved in the correct format.
    *   Run the augmentation cells in `DataCollection.ipynb` to generate the dataset.

2.  **Model Training**:
    *   Open `IrisEstimation.ipynb`.
    *   Run the notebook to load the augmented data, build the model (ResNet50V2 based), and train it.
    *   The model will be saved as `eyetrackerresnet.h5`.

3.  **Real-Time Detection**:
    *   The final section of `IrisEstimation.ipynb` contains a script to run the eye tracker in real-time using your webcam.

## Model Details

The model uses a **ResNet50V2** backbone pretrained on ImageNet, fine-tuned for the regression task of predicting 4 coordinates (x, y for left eye; x, y for right eye) or relevant keypoints.

## Tips for Best Results

*   Ensure good lighting when capturing data.
*   Annotate as accurately as possible.
*   Collect diverse angles and distances to improve model robustness.
