from proximity import match_sites
from notifications import Notifications
from user_input import Person
from aggregator import Site


def main_program():
    """Runs all necessary program functions"""
    person_objects = Person.csv_to_person("res/sample.csv")

    site_objects = Site.csv_to_site()

    matched_dict = match_sites(site_objects, person_objects)
    notifier = Notifications(matched_dict)
    notifier.notify()


main_program()
