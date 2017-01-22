from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "AC9deaae646d9541caaa825c5bb271367c"
auth_token = "4147433dc6a32966c4aa9090737a54f9"
client = TwilioRestClient(account_sid,auth_token)

try:
    message = client.messages.create(body="Hello from Python",
        to="+917600044534",    # Replace with your phone number
        from_="+13524491293") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
    
print(message.sid)

# my twilio number: (858) 375-5852
# number2 (352) 449-1293
# token2 4147433dc6a32966c4aa9090737a54f9
#token1 25a1a27e2d3dfc5062102140d63e57a4
