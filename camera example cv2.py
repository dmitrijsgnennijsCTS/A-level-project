import numpy as np
import cv2

cap = cv2.VideoCapture(0)
haar_cascade = cv2.CascadeClassifier('stop/classifier/cascade.xml')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ##print("repeat")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    s = 0
    #print(len(gray))

    for i in range(len(gray)):
        #print('r',gray[i,0])
        #print('g',gray[i,1])
        #print('b',gray[i,2])
        s = s + gray[i,0] + gray[i,1] + gray[i,2]

    
    s = int(s/(len(gray)*3))

    print(s)

    if s <= 80:
        print('dark')
    #print(gray)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()