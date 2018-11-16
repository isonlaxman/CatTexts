
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACcd838915a43dcca938d2af7fbf145f9e",
"82e487e52ff0bc7d50031e0152a3ecbd")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+16464162961",
                       from_="+16464162961", 
                       body="Hello from Python!")
