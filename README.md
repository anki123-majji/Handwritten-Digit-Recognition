# Handwritten-Digit-Recognition
This project is a real-time handwritten digit recognition system built using Pygame, OpenCV, and a pre-trained deep learning model (Keras). It allows users to draw digits on a virtual board and get immediate predictions of what digit they wrote.

**Features**
A Pygame-based digit drawing interface
Real-time digit prediction using a Keras model
Clears canvas with a single key press
Saves drawn digits as images (optional)

📁 **Project Structure**
├── app.py                  # Main application code
├── bestmodel.keras         # Trained digit recognition model (not included)
├── README.md               # Project documentation

⚙️** Requirements**
  Python 3.x
  pygame
  numpy
  keras
  opencv-python

▶️ How to Run
  Ensure the trained model file (bestmodel.keras) exists at the specified path in the script.
  Run the main script:
      python app.py
  Draw a digit using your mouse.
  Release the mouse button to get the prediction.
  Press the n key to clear the screen.

**Image Processing & Prediction Flowchart**
+--------------------------+
|   User Releases Mouse    |
+--------------------------+
           |
           v
+-----------------------------+
| Extract Drawn Region (ROI) |
+-----------------------------+
           |
           v
+-------------------------+
| Convert ROI to Grayscale |
+-------------------------+
           |
           v
+-----------------------+
| Resize to 28x28 pixels |
+-----------------------+
           |
           v
+-----------------------------+
| Pad Image to Preserve Edges |
+-----------------------------+
           |
           v
+---------------------------+
| Normalize Pixel Values   |
|   (Divide by 255.0)      |
+---------------------------+
           |
           v
+-----------------------------+
| Reshape to (1, 28, 28, 1)   |
+-----------------------------+
           |
           v
+--------------------------+
|   Predict with CNN Model  |
+--------------------------+
           |
           v
+-------------------------------+
|  Get Label with Highest Score |
+-------------------------------+
           |
           v
+------------------------+
| Display Predicted Digit |
+------------------------+

**Overall Workflow of Digit Recognition System**
+--------------------+
|  Start Application |
+--------------------+
          |
          v
+---------------------------+
|  Initialize Pygame Window |
+---------------------------+
          |
          v
+-----------------------------+
|  Load Pre-trained Keras ML |
|         Model              |
+-----------------------------+
          |
          v
+---------------------+
| Wait for User Input |
+---------------------+
          |
          v
+-----------------------------+
| Is Mouse Button Pressed?   |
|       (Start Drawing)      |
+-----------------------------+
          |
          v
+----------------------------+
| Capture Mouse Movements   |
|  & Draw on Pygame Canvas  |
+----------------------------+
          |
          v
+----------------------------+
| Is Mouse Button Released? |
|       (Stop Drawing)      |
+----------------------------+
          |
          v
+-----------------------------+
| Crop Drawn Region from     |
| Canvas (x_min, x_max, ...) |
+-----------------------------+
          |
          v
+-------------------------------+
| Preprocess Image for Model   |
| (Grayscale, Resize, Pad,     |
|  Normalize, Reshape)         |
+-------------------------------+
          |
          v
+---------------------------+
|  Predict Using ML Model  |
+---------------------------+
          |
          v
+-----------------------------+
| Display Prediction on Canvas |
+-----------------------------+
          |
          v
+--------------------------+
|  Press 'n' to Clear      |
+--------------------------+
          |
          v
+--------------------+
|      Repeat        |
+--------------------+
          |
          v
+---------------------+
|        Exit         |
+---------------------+
