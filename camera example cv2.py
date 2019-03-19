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

import numpy as np
import cv2
from PIL import Image

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

calc = 0
#frame = cv2.resize(frame, (1, 1))
for i in range(len(frame)):
    for n in range(len(frame[i])):
        for x in range(len(frame[i][n])):
            calc += frame[i][n][x]
   
print(int(calc/(3*(len(frame)*len(frame[0])))))


































