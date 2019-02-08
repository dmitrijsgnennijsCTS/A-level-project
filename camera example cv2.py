import numpy as np
import numexpr as ne # library numexpr
import cv2
from PIL import Image

cap = cv2.VideoCapture(0)

#cap = cv2.VideoCapture('VID_20181222_210041.mp4')
#haar_cascade = cv2.CascadeClassifier('stop/classifier/cascade.xml')

ret, frame = cap.read()
cv2.imshow('frame2', frame)
#print(frame)
calc = 0
for i in range(len(frame)):
    for n in range(len(frame[i])):
        for x in range(len(frame[i][n])):
            calc += frame[i][n][x]
        #print(frame[i][n])
#frame.resize((1,1))
#print(frame) # Prints the mean colour of the image somehow
#cv2.imshow('frame', frame)
#if cv2.waitKey(1) == 27:
 #   break

# When everything done, release the capture
print(int(calc/(3*(len(frame)*len(frame[0])))))
frame.resize((1,1))
print(frame[0][0]) # Prints the mean colour 
#print(len(frame[0]))
#cap.release()
#cv2.destroyAllWindows()