import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while(True):
	_, frame = cap.read()
	# hue, sat, val .. color range purpose
	hsv_version = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([30,150,50])
	upper_red = np.array([255,255,180])

	# if in range 1, not in range 0 - binary
	mask = cv2.inRange(hsv_version, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('result',res)

	k = cv2.waitKey(5) & 0xFF
	if(k == ord('q')):
		break

cv2.destroyAllWindows()
cap.release()


