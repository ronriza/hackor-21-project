import smtplib
import os
from sms_alert import twilio_notify
# from proximity import match_sites
# from aggregator import Site
# from user_input import Person


class Notifications:
    """contains data members and methods required for sending notifications"""
    def __init__(self, match_dict):
        self.matches = match_dict
        self.notified = {}

    def notify(self):
        """checks if person has been notified and sends notifications based on contact info"""
        for person in self.matches:
            try:
                x = self.notified[person]
            except KeyError:
                location_names = []
                for site in self.matches[person]:
                    location_names.append(site.location)
                locations = "-" + "\n-".join(location_names)
                if person.email:
                    self.email_notify(person, locations)
                if person.phone_number:
                    self.phone_notify(person, locations)
                self.notified[person] = True
            else:
                continue

    @staticmethod
    def email_notify(person, locations):
        """sends email notification"""
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.login('covidvaccinenotification@gmail.com', os.environ['password'])
        conn.sendmail('covidvaccinenotifier@gmail.com', person.email,
                      'Subject: New vaccine availability\n\nWe have found new vaccine '
                      'availability for you at the following locations:\n' + locations)

    @staticmethod
    def phone_notify(person, locations):
        """sends sms notification"""
        twilio_notify(person, locations)


# people_objects = [
#     Person(29, 11105, 20, 'ronriza91@gmail.com', "3479686846"),
#     Person(30, 11372, 20, 'rizar@oregonstate.edu'),
#     Person(20, 12561, 20, 'ronriza91@gmail.com', "3479686846"),
#     Person(15, 13820, 20, 'fakeemail@gmail.com', "2125553333"),
#     Person(25,13902, 20, "blabla@gmail.com", '9998724321')
# ]
#
# site_objects = [
#     Site("Suny Binghamton", "Binghamton, NY", 13902, 32721, "Pfizer", "NA", True),
#     Site("Suny Oneonta", "Oneonta, NY", 13820, 32721, "Pfizer", "NA", True),
#     Site("Javitz Center", "New York, NY", 10001, 32721, "Pfizer", "NA", True),
#     Site("Ulster Fairgrounds", "New Paltz, NY", 12561, 32721, "Pfizer", "NA", True),
#     Site("State Fair Expo Center", "Syracuse, NY", 13209, 32721, "PFizer", "NA", True)
# ]
#
# matched = match_sites(site_objects, people_objects)
# notifier = Notifications(matched)
# notifier.notify()
# notifier.notify()


