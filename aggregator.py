import csv

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

    def __repr__(self):
        return "Site(_name={}, _location={}, _zip_code={}, _last_checked={}, _vaccine_type={}, _facility_type={}," \
               "_availability={}".format(self._name, self._location, self._zip_code, self._last_checked,
                                         self._vaccine_type, self._facility_type, self._availability)

    @staticmethod
    def csv_to_sites(filepath: str) -> list:
        """Returns a list of Site objects generated from a properly formatted CSV located at filepath"""
        res = []
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    name = row[0]
                    location = row[1]
                    zip_code = int(row[2])
                    last_checked = int(row[3])
                    vaccine_type = row[4]
                    facility_type = row[5]
                    availability = bool(row[6])
                    res.append(Site(name, location, zip_code, last_checked, vaccine_type, facility_type, availability))
                except IndexError:
                    if not row:
                        print("Skipping empty row...")
                        continue
                    else:
                        raise
                except ValueError:
                    print("Unable to cast value. Skipping row...")
                    continue

        return res

    @staticmethod
    def sites_to_csv(sites: list, filepath: str):
        """Writes site objects in sites to a CSV file located at filepath. Overwrites any existing file."""
        with open(filepath, "w+") as file:
            writer = csv.writer(file)

            for site in sites:
                writer.writerow(
                    (site.get_name(), site.get_location(), str(site.get_zip_code()), str(site.get_last_checked()),
                     site.get_vaccine_type(), site.get_facility_type(), str(site.get_availability())
                     )
                )
