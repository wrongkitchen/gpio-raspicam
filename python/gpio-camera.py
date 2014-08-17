import time
import picamera
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)

with picamera.PiCamera() as camera:
	camera.start_preview()
	GPIO.wait_for_edge(18, GPIO.FALLING)
	camera.capture('/home/pi/project/gpio-raspicam/photo/image.jpg')
	camera.stop_preview()
	os.system('scp /home/pi/project/gpio-raspicam/photo/image.jpg pi@shaun-mbbc:~/Desktop/pi/cam1.jpg')
