import os
import json
import cv2

# Train set
print("Creating info.dat for train set")
with open("../benchmark_velocity_train/info.dat", 'w') as f:
    f.write("")

for index in os.listdir("../benchmark_velocity_train/clips"):
    path = "../benchmark_velocity_train/clips/" + index

    with open(path + "/annotation.json", 'r') as f:
        annotation = json.load(f)
    
    with open("../benchmark_velocity_train/info.dat", 'a') as f:    
        
        for img in os.listdir(path + "/imgs"):

            filename = path + "/imgs/" + img

            n_cars = "1"
            line = " ".join([filename, n_cars])
            
            x = str(int(annotation[0]['bbox']['left']))
            y = str(int(annotation[0]['bbox']['top']))
            width = str(int(annotation[0]['bbox']['right'] - annotation[0]['bbox']['left']))
            height = str(int(annotation[0]['bbox']['bottom'] - annotation[0]['bbox']['top']))
            line = " ".join([line, x, y, width, height])

            f.write(line + "\n")

# Supplementary set
print("Creating info.dat for supplementary set")
with open("../benchmark_velocity_supp/annotation.json", 'r') as f:
    annotations = json.load(f)

with open("../benchmark_velocity_supp/info.dat", 'w') as f:
    f.write("")

with open("../benchmark_velocity_supp/info.dat", 'a') as f:    
    for annotation in annotations:

        filename = annotation['file_name'].strip("'")
        n_cars = str(len(annotation['bbox']))
        line = " ".join([filename, n_cars])
        
        for box in annotation['bbox']:
            x = str(int(box['left']))
            y = str(int(box['top']))
            width = str(int(box['right'] - box['left']))
            height = str(int(box['bottom'] - box['top']))
            line = " ".join([line, x, y, width, height])

        f.write(line + "\n")

image = cv2.imread("../benchmark_velocity_supp/supp_img/0001.jpg")
print("image shape:", image.shape)

# Negative img paths
print("Creating negatives.txt info file")

with open("../GTI Car Detection Database/negatives.txt", 'w') as f:
    f.write("")

with open("../GTI Car Detection Database/negatives.txt", 'w') as f:

    for folder in os.listdir("../GTI Car Detection Database/non-vehicles"):
        path = "../GTI Car Detection Database/non-vehicles/" + folder

        for img in os.listdir(path):
            f.write("../../../../../UNSW/COMP9517/Project/Individual/GTI Car Detection Database/non-vehicles/" + folder + "/" + img + "\n")