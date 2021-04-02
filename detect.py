import cv2
import os
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys

def detect(img, prediction, show):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    cars = clf.detectMultiScale(gray)

    if show == 1:
        fig, ax = plt.subplots()
        ax.imshow(img)
    
    for (x, y, w, h) in cars:
        # Convert info into dict
        bbox_dict = {}
        bbox_dict["bbox"] = {"top": int(y), "left": int(x), "right": int(x + w), "bottom": int(y + h)}

        if bbox_dict not in prediction:
            prediction.append(bbox_dict)

        if show == 1:
            # Annotate image
            rect = patches.Rectangle((x, y), w, h, color='lime', fill=None)
            ax.add_patch(rect)
    if show == 1:
        plt.show()  

show = 0

if len(sys.argv) > 1:
    show = int(sys.argv[1])

clf = cv2.CascadeClassifier()
clf.load("../classifier/cascade.xml")

clips_path = "../benchmark_velocity_test/clips/"
# Create predictions

for folder in os.listdir(clips_path):
    path = clips_path + folder + "/imgs/"
    prediction = []
   
    img = cv2.imread(path + "040.jpg")
    detect(img, prediction, show)

    # print(prediction)
    with open(clips_path + folder + "/prediction.json", "w") as f:
        json.dump(prediction, f)
