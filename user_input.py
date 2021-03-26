from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    """Represents a Person with the necessary attributes to notify the person of vaccine availability """
    _age: int
    _person_zipcode: int
    _radius: int
    _email: str

    def getAge(self):
        """Returns age of person"""
        return self._age


# test = Person(12, 8854, 3, 'cat@gmail.com')
# print(test.__hash__())


# Need to create logic to cap radius

