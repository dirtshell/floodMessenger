
from twilio.rest import TwilioRestClient
from time import gmtime, strftime
import logging

# Setting up the configurations and what not
# LOGGING CONFIG
logging.basicConfig(filename='sensor.log', level=logging.DEBUG)
# TWILIO CONFIG
account_sid = 'AC3aec37d52f26f2585cdbeda714d45a9c'
auth_token = '71f4f415d16ec2930b99d5a8bd08d7d5'
client = TwilioRestClient(account_sid, auth_token)

# Sends the alert SMS and logs it
def send_alert():
	contacts = ['+13053893667', '+19545947669', '+15712685407']
	date_time = datetime.datetime.now()
	time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	for contact in contacts:
		message = client.messages.create(
			body='ALERT: The flood sensor has been triggered at {0}'.format(time),
			to=contact,
			from_='+15613256723')
	logging.info('ALERT: The flood sensor has been triggered at {0}'.format(time)
	
	
