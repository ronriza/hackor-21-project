import os
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client


def twilio_notify(person, locations):
    """sends user a test messsage via twilio"""
    account_sid = os.environ['twilio_sid']
    auth_token = os.environ['twilio_auth_token']
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body="Vaccine Available!\n" + locations,
            from_='+13343360125',
            to='+1' + person.phone_number
        )
    except TwilioRestException:
        print("The number " + person.phone_number + " is not valid.")

    # print(message.sid)
