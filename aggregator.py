class Site:
    """Site that may or may not have availability"""

    def __init__(self, name: str, location: str, zip_code: int, last_checked: int, vaccine_type: str,
                 facility_type: str, availability: bool):
        """Creates a Site object with the specified attributes"""
        self._name = name
        self._location = location
        self._zip_code = zip_code
        self._last_checked = last_checked
        self._vaccine_type = vaccine_type
        self._facility_type = facility_type
        self._availability = availability

    def get_name(self):
        return self._name

    def get_location(self):
        return self._location

    def get_zip_code(self):
        return self._zip_code

    def get_last_checked(self):
        return self._last_checked

    def get_vaccine_type(self):
        return self._vaccine_type

    def get_facility_type(self):
        return self._facility_type

    def get_availability(self):
        return self._availability

    def set_last_checked(self, value):
        self._last_checked = value

    def set_availability(self, value):
        if not isinstance(value, bool):
            raise ValueError("availability must be bool")
        else:
            self._availability = value
