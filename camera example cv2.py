import numpy as np
import cv2
from PIL import Image

cap = cv2.VideoCapture(0)#'C:/Users/Dmitrijs/Documents/GitHub/A-level-project-/new/n/' + img)
for images in range(3000):
	#img = str(images+1) + ".jpg"
	#print(img)
	#cap = cv2.VideoCapture(0)#'C:/Users/Dmitrijs/Documents/GitHub/A-level-project-/new/n/' + img)
	ret, frame = cap.read()
	frame = cv2.resize(frame, (10, 10))
	#cap = cv2.imread('C:/Users/Dmitrijs/Documents/GitHub/A-level-project-/stop/p/' + img, 0)
	#cv2.imshow('frame',frame)
	calc = 0
	tot = 0
	for i in range(len(frame)):
		#print(frame[i])
		for n in range(len(frame[i])):
			#print(frame[i][n])
			for x in range(len(frame[i][n])):
				#print(frame[i][n][x])
				calc += frame[i][n][x]
				tot +=1

	print(int(calc/tot))


































