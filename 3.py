import tkinter as tk
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import cv2
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)


def init_opengl():
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)


def draw_cube():
    vertices = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


root = tk.Tk()
root.geometry("800x600")
root.title("3D Model Game with Hand Gestures")


model_position = np.array([0.0, 0.0, -5.0])
model_scale = np.array([1.0, 1.0, 1.0])
dismantle = False


def process_gesture(results):
    global model_position, model_scale, dismantle
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Gesture interpretation (simple example based on landmark positions)
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            
            # Movement gesture: Move model based on index finger position
            model_position[0] = (index_tip.x - 0.5) * 10  # X-axis move
            model_position[1] = (index_tip.y - 0.5) * -10  # Y-axis move

            # Resize gesture: Thumb and index pinch changes scale
            distance = np.sqrt((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)
            model_scale = np.array([distance * 10] * 3)

            # Dismantle gesture: Track specific finger configurations (e.g., open palm)
            dismantle = True if thumb_tip.y < index_tip.y else False


def render():
    init_opengl()
    cap = cv2.VideoCapture(0)

    while True:
        # Capture hand data
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        process_gesture(results)
        
        # OpenGL rendering
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glTranslatef(*model_position)
        glScalef(*model_scale)
        draw_cube()
        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(10)

# Run render in a separate thread
import threading
threading.Thread(target=render).start()

root.mainloop()
