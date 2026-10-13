from twilio.rest import Client

import os

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUM = "+1234567890"
TO_NUM = "+91XXXXXXXXXX"


client = Client(account_sid, auth_token)
msg = client.messages.create(
    body="Test alert: Baby monitor SMS working ✅",
    from_=twilio_from,
    to=parent_to
)
print("Sent, SID:", msg.sid)
