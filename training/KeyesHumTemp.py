#!/usr/bin/python
import sys
import Adafruit_DHT

# monitor check variables
dangerReported = False

# gets dictionary of humidity / temperature readings
# TODO: CHECK ACCURACY OF HUMIDITY SENSOR
def getTempHum():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)		# GPIO 4 = Signal
    return {'hum': humidity, 'temp': temperature}

# checks if temperature / humidity are within safe parameters
def checkTempHum(tempHum):
    isSafe = tempHum['hum']<30 or tempHum['temp']<19
    if isSafe:
        return {'sys':True, 'read':'SAFE'}
    else:
        return {'sys':False, 'read':'NOT SAFE'}

# Reset monitor check variables after handling danger
def handleDanger():
    dangerReported = False

# Monitor loop
while True:

    tempHum = getTempHum()
    safeReport = checkTempHum(tempHum)

    if not safeReport['sys'] and not dangerReported:
        # Operating at non-optimal humidity / temperature ratio
        # Report and check immediately
        print("nop")
        dangerReported = True

    if dangerReported and safeReport['sys']:
        # False alarm
        print("yap")
        dangerReported = False

    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %  [ {2!s} ]'.format(tempHum['temp'], tempHum['hum'], safeReport['read']))
