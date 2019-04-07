import numpy as np
from PIL import ImageGrab
import cv2
import time

def process_img(original_image):

    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

def screen_record(): 
    #last_time = time.time()
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,95,1024,730)))
        new_screen = process_img(printscreen)
        #print('loop took {} seconds'.format(time.time()-last_time))
        #last_time = time.time()
        cv2.imshow('window',new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
screen_record()