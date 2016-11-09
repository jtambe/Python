import sys
from twilio.rest import TwilioRestClient

client = TwilioRestClient(account='xxxxx', token='xxxxx')

client.messages.create(from_="xxxxxxxxxx", to="xxxxxxxxxx", body="sms from python")


/*
on ubuntu machine use following commands

1. sudo pip install twilio
2. create given file
3. use your account credentials in place of xxxxxxx
4. keep file executable. one way to do it is run command : chmod 777 SMSTwlioService.py
5. execute file python SMSTwilioService.py
*/
