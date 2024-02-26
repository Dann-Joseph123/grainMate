import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from keras.models import load_model

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model("/Users/Dann/Downloads/hand-gesture-recognition-code/mp_hand_gesture")

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)