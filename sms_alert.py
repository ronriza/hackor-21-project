import os

from twilio.rest import Client


def twilio_notify(person, locations):
    account_sid = os.environ['twilio_sid']
    auth_token = os.environ['twilio_auth_token']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Vaccine Available!\n" + locations,
        from_='+13343360125',
        to='+1' + person.phone_number
    )

    print(message.sid)
