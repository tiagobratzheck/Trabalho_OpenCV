import urllib
import numpy as np
import cv2
import os
import os

for file_type in ['positives']:
    for img in os.listdir(file_type):
        os.rename(file_type+"/"+img, file_type + "/"+img.replace(" ", ""))

for file_type in ['negatives']:
    for img in os.listdir(file_type):
        os.rename(file_type+"/"+img, file_type + "/"+img.replace(" ", ""))