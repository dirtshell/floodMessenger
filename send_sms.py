
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
	date_time = datetime.datetime.now()
	time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	message = client.messages.create(
		body='ALERT: The flood sensor has been triggered at {0}'.format(time),
		to='+13053893667',
		from_='+15613256723')
	logging.info('ALERT: The flood sensor has been triggered at {0}'.format(time)
	
	
