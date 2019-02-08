import numpy as np
import cv2
from PIL import Image

cap = cv2.VideoCapture(0)

#cap = cv2.VideoCapture('VID_20181222_210041.mp4')
#haar_cascade = cv2.CascadeClassifier('stop/classifier/cascade.xml')
while(True):
    ret, frame = cap.read()
    frame2 = frame.resize((1,1))
    print(frame2[0][0]) # Prints the darkness of image
    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

















