from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

client = Client(account_sid, auth_token)

call = client.calls.create(
    to= os.getenv("to"),
    from_= os.getenv("from_"),
    # Inline TwiML that speaks a message
    twiml='<Response><Say>HOW are you</Say></Response>'
)

print("Call SID:", call.sid)
