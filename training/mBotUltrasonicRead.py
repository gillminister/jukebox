import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

SIG = 14

GPIO.setup(SIG,GPIO.IN)
#GPIO.output(RED,0)
#GPIO.setup(GREEN,GPIO.OUT)
#GPIO.output(GREEN,0)
#GPIO.setup(BLUE,GPIO.OUT)
#GPIO.output(BLUE,0)

#try:
while (True):
    print(GPIO.input(SIG))
