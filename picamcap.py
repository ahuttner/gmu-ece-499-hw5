import time
import cv2
import numpy as np
import io
import sys
import os

try:
        color = sys.argv[1]
        print "Chosen color is: ", color

        BlueL = np.array([100,50,50],np.uint8)
        BlueH = np.array([140,255,255],np.uint8)
        RedL = np.array([0,50,50],np.uint8)
        RedH = np.array([20,255,255],np.uint8)
        GreenL = np.array([40,50,50],np.uint8)
        GreenH = np.array([80,255,255],np.uint8)

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

        cap = cv2.VideoCapture(0)

        while True:
                ret, frame = cap.read()
                hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv,Low,High)
                M = cv2.moments(mask)
                if M['m00'] == 0:
                        print "cx and cy will both be 0"
                        cx = 0
                        cy = 0
                else:
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                cv2.imshow('Mask',mask)
                cv2.waitKey(5)
                if cx > 300 and cx < 340:
                        print "Centered"
                        os.system("python send_wheel.py " + 's')
                elif cx < 300 and cx > 0:
                        print "Object to left, move left"
                        os.system("python send_wheel.py " + 'a')
                elif cx > 340:
                        print "Object to right, move right"
                        os.system("python send_wheel.py " + 'd')
                else:
                        print "Stop"
                        os.system("python send_wheel.py " + 's')

except KeyboardInterrupt:
        os.system("python send_wheel.py "+'s')
