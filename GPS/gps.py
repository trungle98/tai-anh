import serial
import syslog
import time

#The following line is for serial over GPIO
port = '/dev/ttyUSB0' # note I'm using Mac OS-X


ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

i = 0

while (True):
    # Serial read section
	data = ard.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print(data)
