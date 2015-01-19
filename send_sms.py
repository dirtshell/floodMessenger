from twilio.rest import TwilioRestClient
from time import strftime
import logging
import time
import RPi.GPIO as GPIO
import datetime

# Setting up the configurations and what not
# RASBERRY PI CONFIG
INPUT_PIN = 18  # The BCM pin the current switch is connected to
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # High by default

# LOGGING CONFIG
logging.basicConfig(filename='sensor.log', level=logging.DEBUG)

# TWILIO CONFIG
account_sid = 'AC3aec37d52f26f2585cdbeda714d45a9c'
auth_token = '71f4f415d16ec2930b99d5a8bd08d7d5'
client = TwilioRestClient(account_sid, auth_token)

# Sends the alert SMS and logs it
def send_alert(channel):
	contacts = ['+13053893667', '+19545947669', '+15712685407']
	time = strftime("%Y-%m-%d %H:%M:%S")
	for contact in contacts:
		message = client.messages.create(
			body='ALERT: The flood sensor has been triggered at {0}'.format(time),
			to=contact,
			from_='+15613256723')
	logging.info('ALERT: The flood sensor has been triggered at {0}'.format(time))
	print 'FLOOD DETECTED'
	
# Main loop
GPIO.add_event_detect(INPUT_PIN, GPIO.FALLING, callback=send_alert, bouncetime=600) # Listen for press
while True:
	print 'Waiting for something to report...'
	time.sleep(6000)

GPIO.cleanup()
