import numpy as np
import cv2

cap = cv2.VideoCapture(0)
haar_cascade = cv2.CascadeClassifier('stop/classifier/cascade.xml')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    z = frame.reshape((-1, 3))
    z = np.float32(z)
    criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)
    ret, label, center = cv2.kmeans(z, 4, None, criteria, 10, 0)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((frame.shape))
    cv2.imshow('preview', res2)

    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()