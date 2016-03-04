from picamera.array import PiRGBArray
from picamera import PiCamera 
import picamera 
import time 
import cv2 
import numpy as np 
import io 
import sys 
import os


color = sys.argv[1]
print "Chosen color is: ", color

BlueL = np.array([100,50,50])
BlueH = np.array([140,255,255])
RedL = np.array([0,50,50])
RedH = np.array([20,255,255])
GreenL = np.array([40,100,50])
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

cam = PiCamera()

cam.vflip = True
cam.hflip = True

cam.resolution = (320,240)

try:
	while True:
		cap = PiRGBArray(cam)

		cam.capture(cap,format="bgr")

		im = cap.array
		imHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
		imRang = cv2.inRange(imHSV,Low,High)
#		print imRang
#		cv2.imshow("Range",imRang)
		cv2.waitKey(5)
		
		if color == 'R' or color == 'r':
			if np.mean(imRang) > 10:
				#Centering
				NonZ = np.nonzero(imRang)
				#Find center of mass
				moment = cv2.moments(imRang) #Imrang exchanged for NonZ
				center =int(moment['m10']/moment['m00'])
				print "Center X is: ",center
				if center == 160:
					os.system("python SendWheel.py "+'s')
				elif center < 160:
					os.system("python SendWheel.py "+'a')
				else:
					os.system("python SendWheel.py "+'s')
				print "It's gettin hot in hurr"
			else:
				 os.system("python SendWheel.py "+'a')
		#If it is onscreen, center it	
		elif np.mean(imRang) > 5:
			#Centering
			NonZ = np.nonzero(imRang)
			moment = cv2.moments(imRang) #imRang exchanged for NonZ
			center = int(moment['m10']/moment['m00'])
			print "Center X is: ",center
			if center == 160:
				os.system("python SendWheel.py "+'s')
			elif center < 160:
				os.system("python SendWheel.py "+'a')
			else:
				os.system("python SendWheel.py "+'s')
			print "Fuck Yeah, it be hurr"
		#If not there pivot to look for it
		else:
			os.system("python SendWheel.py " +'d')

	
except KeyboardInterrupt:		
	os.system("python SendWheel.py "+'s')

