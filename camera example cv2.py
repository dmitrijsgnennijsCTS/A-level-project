import numpy as np
import numexpr as ne # library numexpr
import cv2

cap = cv2.VideoCapture('VID_20181222_210041.mp4')
haar_cascade = cv2.CascadeClassifier('stop/classifier/cascade.xml')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    a2D = frame.reshape(-1, frame.shape[-1])
    col_range= (256, 256, 256)
    eval_params = {'a0':a2D[:,0], 'a1':a2D[:,1], 'a2':a2D[:,2], 's0': col_range[0], 's1': col_range[1]}
    a1D = ne.evaluate('a0*s0*s1+a1*s0+a2', eval_params)
    print(np.unravel_index(np.bincount(a1D).argmax(), col_range))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()