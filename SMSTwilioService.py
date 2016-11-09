import sys
from twilio.rest import TwilioRestClient

client = TwilioRestClient(account='xxxxx', token='xxxxx')

client.messages.create(from_="xxxxxxxxxx", to="xxxxxxxxxx", body="sms from python")
