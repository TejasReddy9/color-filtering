import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,300);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,400);

while(True):
	_, frame = cap.read()
	# hue, sat, val .. color range purpose
	hsv_version = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	## only for red -30 to 0 and 0 to 30 -  2masks
	lower_red = np.array([150,50,50])
	upper_red = np.array([180,255,255])
	mask1 = cv2.inRange(hsv_version, lower_red, upper_red)

	lower_red = np.array([0,50,50])
	upper_red = np.array([30,255,255])
	mask2 = cv2.inRange(hsv_version, lower_red, upper_red)

	mask = cv2.bitwise_or(mask1,mask2)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	##averaging
	kernel = np.ones((10,10), np.float)/100
	smoothened = cv2.filter2D(res, -1, kernel)
	bilateral = cv2.bilateralFilter(res, 10, 75, 75)

	cv2.imshow('frame',frame)
	cv2.imshow('result',res)
	cv2.imshow('smoothened', smoothened)
	cv2.imshow('bilateral',bilateral)

	k = cv2.waitKey(3) & 0xFF
	if(k == 27):
		break

cv2.destroyAllWindows()
cap.release()


