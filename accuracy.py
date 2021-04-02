import os
from velocity import VeloEval
import json

dataset_path = "../benchmark_velocity_test/clips/"

folder_path = os.listdir(dataset_path)
annotations = [os.path.join(dataset_path, x, 'annotation.json') for x in folder_path]
predictions = [os.path.join(dataset_path, x, 'prediction.json') for x in folder_path]
img_paths = [os.path.join(dataset_path, x, 'imgs/040.jpg') for x in folder_path]

gt = VeloEval.load_annotation(annotations)
pred = VeloEval.load_annotation(predictions)

VeloEval.accuracy(pred, gt, img_paths)