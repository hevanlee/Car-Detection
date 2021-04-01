import cv2
import os
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    cars = clf.detectMultiScale(gray)

    print(cars)
    
    fig, ax = plt.subplots()
    ax.imshow(img)
    
    for (x, y, w, h) in cars:
        
        rect = patches.Rectangle((x, y), w, h, color='red', fill=None)
        ax.add_patch(rect)
    
    plt.show()



clf = cv2.CascadeClassifier()
clf.load("../clf1/cascade.xml")

clips_path = "../benchmark_velocity_test/clips/"
for folder in os.listdir(clips_path):
    path = clips_path + folder + "/imgs/"

    for jpg in os.listdir(path):
        img = cv2.imread(path + jpg)
        detect(img)