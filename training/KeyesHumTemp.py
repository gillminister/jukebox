#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Adafruit_DHT
import smtplib



# monitor check variables
dangerReported = False
tempThreshold = 19
humThreshold = 30

# gets dictionary of humidity / temperature readings
# TODO: CHECK ACCURACY OF HUMIDITY SENSOR
def getTempHum():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)		# GPIO 4 = Signal
    return {'hum': humidity, 'temp': temperature}

# checks if temperature / humidity are within safe parameters
def checkTempHum(tempHum):
    isSafe = tempHum['hum'] < humThreshold or tempHum['temp'] < tempThreshold
    if isSafe:
        return {'sys':True, 'read':'SAFE'}
    else:
        return {'sys':False, 'read':'NOT SAFE'}

# Reset monitor check variables after handling danger
def handleDanger():
    dangerReported = False

#######################################################
## ---------------- Email notifiers ---------------- ##
#######################################################
# Notifiy that environment is unacceptable
def notifyDanger(humTemp, isDanger):
    # authenthicate gmail user
    gmail_user = 'dendril.notifier@gmail.com'
    gmail_password = 'lettPassord'  #'S#Y^yV(rAk)7R*bw'

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
    except:
        print('ERR:\tcould not authenthicate gmail login')

    # generate and send email
    sent_from = gmail_user
    to = ['jorn91@gmail.com', 'emiliehtakacs@gmail.com']
    subject = 'Fuktig gang!'
	body = None
	if isDanger:
	    body = 'Gangen hold no {0:0.1f}C {1:0.1f}% fukt. Sjekk måler og gjennomtrekk.'.format(humTemp['temp'], humTemp['hum'])
	else:
		body = 'Gangen har returnert til normal.'

    email_text = """\
From: {0!s}
To: {1!s}
Subject: {2!s}

{3!s}
""".format(sent_from, ", ".join(to), subject, body)

    try:
        print(1)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print(2)
        server.ehlo()
        print(3)
        server.login(gmail_user, gmail_password)
        print(4)
        #server.sendmail(sent_from, to, email_text)
        server.sendmail("""\
From: dendril.notifier@gmail.com
To: jorn91@gmail.com
Subject: TestTest
Borat
""")
        print(5)
        #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #server.ehlo()
        #server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        dangerReported = isDanger
        print('SUCC:\tDanger notification email sent!')
    except:
        print("ERR:\tcould not send email")


# Monitor loop
while True:
    tempHum = getTempHum()
    safeReport = checkTempHum(tempHum)

    if not safeReport['sys'] and not dangerReported:
        # Operating at non-optimal humidity / temperature ratio
        # Report and check immediately
        notifyDanger(tempHum, True)

    if dangerReported and safeReport['sys']:
        # False alarm
		# Report return to normality
		notifyDanger(tempHum, False)

    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %  [ {2!s} ]'.format(tempHum['temp'], tempHum['hum'], safeReport['read']))
