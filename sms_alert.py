import os

from twilio.rest import Client


def phone_notify(self):
    account_sid = os.environ['twilio_sid']
    auth_token = os.environ['twilio_auth_token']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Vaccine Available!",
        from_='+13343360125',
        to='+1' #phone number
    )

    print(message.sid)
