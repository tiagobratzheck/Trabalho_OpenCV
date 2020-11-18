import numpy as np
import cv2


def vi_detector(path):

    camera = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier(path)

    while True:
        _,img = camera.read()
        height, width, c = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        objects = cascade.detectMultiScale(gray, 1.2, 5)
        print(objects)
        for (x,y,w,h) in objects:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('Image:', img)
        k = cv2.waitKey(60)
        if k==27:
            break

    camera.release()
    cv2.destroyAllWindows()

