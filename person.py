from dataclasses import dataclass
import csv


@dataclass(frozen=True)
class Person:
    """Represents a Person with the necessary attributes to notify the person of vaccine availability"""
    _age: int
    _person_zipcode: int
    _radius: int
    _email: str = ""
    _phone_number: str = ""

    def get_age(self):
        """Returns age of person"""
        return self._age

    def get_person_zipcode(self):
        """Returns zipcode of person"""
        return self._person_zipcode

    def get_radius(self):
        """Returns radius to search"""
        return self._radius

    def get_email(self):
        """Returns email of person"""
        return self._email

    def get_phone_number(self):
        """Returns phone number of person"""
        return self._phone_number

    @property
    def age(self) -> int:
        return self._age

    @property
    def zip_code(self) -> int:
        return self._person_zipcode

    @property
    def radius(self) -> int:
        return self._radius

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @staticmethod
    def csv_to_person(filepath: str) -> list:
        """Returns a list of Person objects from a correctly formatted CSV file located at filepath"""
        object_list = []
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    age = int(row[0])
                    zip_ = int(row[1])
                    radius = int(row[2])
                    email = row[3]
                    phone = row[4]
                    object_list.append(Person(age, zip_, radius, email, phone))
                except ValueError:
                    print("Unable to cast value. Skipping row...")
                    continue

        return object_list
