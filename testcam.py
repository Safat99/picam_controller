import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
	print('Cannot open camera')
	exit()

while(True):
	ret , frame = cap.read()
	frame = cv2.resize(frame, (640,480))
	if not ret:
		print('Can\'t receive frame....Exiting')
		break

	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# backtorgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
	# cv2.imshow('gray', gray)
	cv2.imshow('frame',  frame)
	# cv2.imshow('backtorgb', backtorgb)
	if cv2.waitKey(1) ==  ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
