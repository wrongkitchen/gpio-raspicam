import time
import picamera
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)

with picamera.PiCamera() as camera:
	camera.start_preview()
	GPIO.wait_for_edge(18, GPIO.FALLING)
	camera.capture('/home/pi/project/py-gpio/photo/image.jpg')
	os.system('scp /home/pi/project/py-gpio/photo/image.jpg admin@wrongkitchen.mycloudnas.com:/share/HDA_DATA/Qweb/scp2/cam1_123.jpg')
	camera.stop_preview()
