import serial
import sys

port = serial.Serial('/dev/ttyACM0',1000000)

data = sys.argv[1]

port.write(data)
