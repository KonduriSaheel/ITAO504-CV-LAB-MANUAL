import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print("Current folder:", os.getcwd())

img = cv2.imread(os.path.join(os.getcwd(), "input.jpg"))

if img is None:
    print("Image not found!")
    exit()
else:
    print("Image loaded successfully!")