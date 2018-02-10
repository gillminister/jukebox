#!/usr/bin/python
import sys
import Adafruit_DHT

def getTempHum():
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)		# GPIO 4 = Signal
	return {'hum': humidity, 'temp': temperature}

def checkTempHum():
	return False

while True:

    tempHum = getTempHum()

    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(tempHum['temp'], tempHum['hum']))
