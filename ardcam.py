import serial
import cv2
import time
ArduinoSerial = serial.Serial('com3',9600) 
time.sleep(2) 
while 1:
    incoming = str (ArduinoSerial.readline()) 
    print(incoming)
 
    if 'hello' in incoming:
        # define a video capture object
        vid = cv2.VideoCapture(0)
        while(True):
	        ret, frame = vid.read()
	        cv2.imshow('frame', frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
		        break
        vid.release()
        cv2.destroyAllWindows()
    incoming = "";      