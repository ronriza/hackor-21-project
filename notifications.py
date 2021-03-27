import smtplib
from test import Person
from sms_alert import twilio_notify

class Notifications:

    def __init__(self, match_dict):
        self.matches = match_dict
        self.notified = {}

    def notify(self):
        for person in self.matches:
            try:
                x = self.notified[person]
            except KeyError:
                locations = "\n".join(self.matches[person])
                if person._email:
                    self.email_notify(person, locations)
                if person._number:
                    self.phone_notify(person, locations)
                self.notified[person] = True
            else:
                continue

    def email_notify(self, person, locations):

        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.login('covidvaccinenotification@gmail.com', 'Hackor21')
        conn.sendmail('covidvaccinenotifier@gmail.com', person._email,
                      'Subject: New vaccine availability\n\nWe have found new vaccine '
                      'availability for you in the following locations:\n' + locations)

    def phone_notify(self, person, locations):
        twilio_notify(person, locations)

dictionary = {Person('ronriza91@gmail.com'): ["Javitz", "Suny"],
        Person('rizar@oregonstate.edu'): ["Javitz", "Suny"]}
notifier = Notifications(dictionary)
notifier.notify()
notifier.notify()








