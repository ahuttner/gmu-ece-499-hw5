from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import time
import cv2
import numpy as np
import io
import sys

color = sys.argv[1]
print "Chosen color is: ", color

BlueL = np.array([100,50,50])
BlueH = np.array([140,255,255])
RedL = np.array([0,50,50])
RedH = np.array([20,255,255])
GreenL = np.array([40,50,50])
GreenH = np.array([80,255,255])

Low = ([0,0,0])
High = ([255,255,255])

if color == 'r' or color ==  'R':
	Low = RedL
	High = RedH
elif color  == 'g' or color == 'G':
	Low = GreenL
	High = GreenH
elif color == 'b' or color == 'B':
	Low = BlueL
	High = BlueH
#else:	low = ([0,0,0])
#	High = ([255,255,255])

cam = PiCamera()

cam.vflip = True
cam.hflip = True

#cam.start_preview()

while True:
	cap = PiRGBArray(cam)

#	time.sleep(0.01)

	cam.capture(cap,format="bgr")

	im = cap.array
	imHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
	imRang = cv2.inRange(imHSV,Low,High)

#	cv2.imshow("Cam",imHSV)
	cv2.imshow("Range",imRang)
	cv2.waitKey(5)

