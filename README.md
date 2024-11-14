# 3D-Model-Game-with-Hand-Gesture-Control-Using-Python-OpenGL-and-MediaPipe
I developed a unique 3D game experience using Python, integrating OpenGL for 3D rendering and MediaPipe for hand gesture recognition. The project allows users to interact with a 3D model—a cube—through hand gestures, captured in real time via a webcam.

# 3D Model Game with Hand Gesture Control

This Python project integrates OpenGL for 3D rendering with MediaPipe for real-time hand gesture recognition, creating an interactive 3D environment where users control a 3D cube using hand gestures. The application captures gestures through a webcam, allowing natural interaction with the virtual model in real time.

## Features

- **Hand Gesture Control**: Move, scale, and dismantle the 3D model based on hand gestures.
- **Real-Time Interaction**: Uses MediaPipe and OpenCV for live video feed processing and gesture interpretation.
- **3D Graphics**: Renders a movable and scalable 3D cube in an OpenGL environment.
- **User Interface**: Built with Tkinter to provide a simple GUI.

## Requirements

To run this project, you'll need:
- Python 3.x
- Required Libraries:
  ```bash
  pip install pygame opencv-python mediapipe numpy PyOpenGL tk
  ```

## How It Works

1. **Initialization**: 
   - Initializes the OpenGL environment using Pygame.
   - Sets the camera view and initial position.

2. **3D Cube Creation**:
   - Defines vertices and edges to render a wireframe cube in 3D space.
   - Uses OpenGL’s `GL_LINES` to draw the edges of the cube.

3. **Gesture Processing**:
   - Uses MediaPipe’s hand tracking to detect and interpret hand gestures from webcam input.
   - Key gestures:
     - **Move Gesture**: The cube moves based on the position of the index finger.
     - **Scale Gesture**: Pinching the thumb and index finger resizes the cube.
     - **Dismantle Gesture**: An open palm dismantles the cube (activates a Boolean flag).

4. **Rendering**:
   - Runs a loop to capture frames, process hand data, and render the 3D model based on detected gestures.
   - Uses OpenGL to update the cube’s position and size based on gesture inputs.

5. **Multithreading**:
   - Runs the rendering in a separate thread to keep the Tkinter GUI responsive while continuously updating the 3D environment.

## Code Breakdown

### 1. Libraries and Hand Tracking Setup

- Imports necessary libraries (Tkinter, OpenGL, Pygame, OpenCV, MediaPipe, and NumPy).
- Initializes MediaPipe’s hand tracking module to detect gestures.

### 2. `init_opengl` Function

- Sets up an OpenGL display and camera perspective for 3D rendering.
  
### 3. `draw_cube` Function

- Defines the vertices and edges of a 3D cube.
- Renders the cube using lines to connect vertices.

### 4. `process_gesture` Function

- Analyzes hand landmarks to detect gestures and apply transformations:
  - **Position**: Updates the cube’s X and Y position based on index finger position.
  - **Scale**: Adjusts the cube’s scale based on thumb-index distance.
  - **Dismantle**: Activates when an open palm is detected.

### 5. `render` Function

- Initializes OpenGL for 3D rendering and captures live video from the webcam.
- Continuously processes frames, detects gestures, and renders the transformed cube in real-time.

### 6. Tkinter GUI and Multithreading

- Runs the rendering in a separate thread so that the Tkinter GUI remains responsive.

## Running the Project

To run this application:
1. Clone the repository and navigate to the project directory.
2. Install the required libraries.
3. Run the Python script:
   ```bash
   python <script_name>.py
   ```
4. Ensure your webcam is enabled for hand gesture detection.

## Demo

![Demo of 3D Cube with Hand Gesture Control](link-to-demo.gif)

## Future Improvements

- Add more gesture types to expand control options.
- Implement additional 3D models and animations.
- Enhance GUI for more user control.

---

This README provides a thorough overview and should make your project accessible to anyone who wants to understand or contribute to it!
