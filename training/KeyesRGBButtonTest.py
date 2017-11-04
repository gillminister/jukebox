import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)


RED = 23
GREEN = 24
BLUE = 25

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

try:
    while (True):
        input_state = GPIO.input(22)
	if input_state == False:
            print "Button pressed, requesting RGB for LED"
            print "Format : ABC Where A = Red, B = Green, C = Blue"
            request = raw_input("RGB-->")
            if (len(request) == 3):
                GPIO.output(RED,int(request[0]))
                GPIO.output(GREEN,int(request[1]))
                GPIO.output(BLUE,int(request[2]))
                print "Thank you. LED updated"
            else:
                print "You fucked up. Format: ABC Where A = Red, B = Green, C = Blue"
                print "Example: 010 for Green"


except KeyboardInterrupt:
    GPIO.cleanup()
