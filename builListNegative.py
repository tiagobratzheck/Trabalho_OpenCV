import urllib
import numpy as np
import cv2
import os

for file_type in ['handFiles/negatives']:
    for img in os.listdir(file_type):
        line = file_type+'/'+img+'\n'
        with open('negatives.txt','a') as f:
            f.write(line)

for file_type in ['peopleFiles/negatives']:
    for img in os.listdir(file_type):
        line = file_type+'/'+img+'\n'
        with open('negatives.txt','a') as f:
            f.write(line)

for file_type in ['truckFiles/negatives']:
    for img in os.listdir(file_type):
        line = file_type+'/'+img+'\n'
        with open('negatives.txt','a') as f:
            f.write(line)