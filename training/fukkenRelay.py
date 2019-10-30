#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#import Adafruit_DHT
import smtplib

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RELAY1 = 19
RELAY2 = 26
RELAY3 = 13

#RED = 17
#GREEN = 27
#BLUE = 22

GPIO.setup(RELAY1, GPIO.OUT)
GPIO.output(RELAY1, 0)

GPIO.setup(RELAY2, GPIO.OUT)
GPIO.output(RELAY2, 0)

GPIO.setup(RELAY3, GPIO.OUT)
GPIO.output(RELAY3, 0)

#GPIO.setup(RED,GPIO.OUT)
#GPIO.output(RED,0)
#GPIO.setup(GREEN,GPIO.OUT)
#GPIO.output(GREEN,0)
#GPIO.setup(BLUE,GPIO.OUT)
#GPIO.output(BLUE,0)

#WARNING = 0
#DANGER = -2


# gets dictionary of humidity / temperature readings
# TODO: CHECK ACCURACY OF HUMIDITY SENSOR
#def getTempHum():
#    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)		# GPIO 4 = Signal
#    return {'hum': humidity, 'temp': temperature}




# Monitor loop
#while True:
#    temp = getTempHum()['temp']
#    if temp <= WARNING and temp > DANGER:
#	GPIO.output(RED, 1)
#	GPIO.output(BLUE, 1)
#	GPIO.output(GREEN, 0)
#    elif temp <= DANGER:
#	GPIO.output(RED, 1)
#	GPIO.output(GREEN, 0)
#	GPIO.output(BLUE, 0)
#    else:
#	GPIO.output(RED, 0)
#	GPIO.output(BLUE, 0)
#	GPIO.output(GREEN, 0)
#    print(temp)

    #print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %  [ {2!s} ]'.format(tempHum['temp'], tempHum['hum'], safeReport['read']))
