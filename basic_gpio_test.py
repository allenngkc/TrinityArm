import RPi.GPIO as GPIO; 

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

while (True): 
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
