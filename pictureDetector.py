import numpy as np
import cv2


def pic_detector(path, picture):

    cascade = cv2.CascadeClassifier(path)
    img = cv2.imread(picture)
    height, width, c = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(gray, 1.2, 5)
    print(objects)
    for (x,y,w,h) in objects:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('Image: ', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

