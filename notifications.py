import smtplib
import os
from sms_alert import twilio_notify


class Notifications:
    """contains data members and methods required for sending notifications"""
    def __init__(self, match_dict):
        self.matches = match_dict
        self.notified = {}

    def notify(self):
        """checks if person has been notified and sends notifications based on contact info"""
        for person in self.matches:
            try:
                # if user was not already notified, a KeyError would be raised here
                x = self.notified[person]
            except KeyError:
                # build a list of available locations from matches dict
                location_names = []
                for site in self.matches[person]:
                    location = site.get_name()
                    location_names.append(location)
                locations = "-" + "\n-".join(location_names)
                if person.email:
                    # if person chose to have emails sent to them
                    self.email_notify(person, locations)
                if person.phone_number:
                    # if person chose to have phone notifications sent to them
                    self.phone_notify(person, locations)
                # add person to notified dict
                self.notified[person] = True
            else:
                continue

    @staticmethod
    def email_notify(person, locations):
        """sends email notification"""
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        try:
            conn.login('covidvaccinenotification@gmail.com', os.environ['password'])
            conn.sendmail('covidvaccinenotifier@gmail.com', person.email,
                          'Subject: New vaccine availability\n\nWe have found new vaccine '
                          'availability for you at the following locations:\n' + locations)
        except KeyError:
            print("password environment variable not set. Unable to send email.")

    @staticmethod
    def phone_notify(person, locations):
        """sends sms notification"""
        twilio_notify(person, locations)
