import json
import cv2

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
            x = str(box['left'])
            y = str(box['top'])
            width = str(box['right'] - box['left'])
            height = str(box['bottom'] - box['top'])
            line = " ".join([line, x, y, width, height])

        f.write(line + "\n")

image = cv2.imread("../benchmark_velocity_supp/supp_img/0001.jpg")
print(image.shape)