import cv2 
import numpy as np

cascade="haarcascade_frontalface_default.xml"

vid=cv2.VideoCapture(0)
# webcam is the default

while True:
    status, frame = vid.read()
    greyframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=cascade.detectMultiScale(greyframe,scaleFactor=1.1,minNeighbors=9)
    #minNeighbors is a  so spelling must be consistent 
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    # status is whether or not there IS any frame to be read, the secondary data being collected is one frame at a time itself
    if status==False:
        break 
    cv2.imshow("Webcam",frame)
    key=cv2.waitKey(10)
    if key==27:
        break 

vid.release()

cv2.destroyAllWindows()


