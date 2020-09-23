import RPi.GPIO as GPIO
import time
from sys import exit
#SETUP
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, 0)

#EXECUTION
try:
	while True:
		GPIO.wait_for_edge(11, GPIO.RISING)
		GPIO.output(13, not GPIO.input(13))
		time.sleep(0.05)
except KeyboardInterrupt: #to stop press cntrl c and the button again
	GPIO.output(13, 0) #led off
	GPIO.cleanup() #cleanup
	exit(0)
