
from twilio.rest import Client

TWILIO_SID = "AC0ea8339a38c9b250f2e3bb823344b0bf"
TWILIO_AUTH_TOKEN = "8df4b923004588e3dbf26a61a461fa81"
TWILIO_VIRTUAL_NUMBER = "+18886228050"
TWILIO_VERIFIED_NUMBER = "+1 253 273 3480"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)