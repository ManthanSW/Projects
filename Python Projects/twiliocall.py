import os 
from twilio.rest import Client

client=Client("AC80dec1f69c0ec09d170e7b2453011684","9b577fcbc3487b0d8cbba9f419fa1b55")

call=client.calls.create(
	to="+919359122902",
	from_="+12057368092",
	url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)