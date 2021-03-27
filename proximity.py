import csv
import pickle
from dataclasses import dataclass
from math import radians, sqrt, sin, cos, asin
from os import path


@dataclass(frozen=True)
class Coordinates:
    """Represents a pair of latitude & longitude horizontal coordinates"""
    _lat: float
    _lon: float

    @property
    def lat(self) -> float:
        return self._lat

    @property
    def lon(self) -> float:
        return self._lon

    def distance(self, other) -> float:
        """Returns the distance in miles between this pair of coordinates and another pair of coordinates"""
        if not isinstance(other, Coordinates):
            return NotImplemented
        else:
            # use the haversine function to calculate the spherical distance between coordinate pairs
            # implemented from https://en.wikipedia.org/wiki/Haversine_formula

            # mean radius calculated by NASA 6371.00 km = 3958.76 mi (formula: 100,000.00 mi = 160,934.40 km)
            # Source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
            # earth_radius = 3958.76
            earth_radius = 6373.0

            # get coordinates in radians
            phi_1 = radians(self.lat)
            phi_2 = radians(other.lat)
            lam_1 = radians(self.lon)
            lam_2 = radians(other.lon)

            sin_squared_lat = sin((phi_2 - phi_1) / 2) ** 2
            sin_squared_lon = sin((lam_2 - lam_1) / 2) ** 2

            return 2 * earth_radius * asin(sqrt(sin_squared_lat + cos(phi_1) * cos(phi_2) * sin_squared_lon))


def zip_code_distance_matrix() -> dict:
    """Returns a dictionary of (zip, zip) -> distance pairs"""

    # TODO: Avoid using pickle
    matrix_file = "res/ZipCodeDistanceMatrix.dat"

    if path.exists(matrix_file):
        with open(matrix_file, "rb") as file:
            zip_code_distances = pickle.load(file)
    else:
        # build a state -> {zip -> coord} dictionary and write it to a json
        zip_code_coords_by_state = {}

        with open("res/ZipCodeSourceData.csv", 'r') as zips:
            # File is tab-delimited. We only care about the data in the following columns:
            #  Col#   2     3     4          5         10    11
            #  Data  ZIP  City  State   State-Abbr.   Lat    Lon
            reader = csv.reader(zips, delimiter='\t')

            # organize zip code data by state
            for row in reader:
                try:
                    zip_code, state, lat, lon = int(row[1]), row[4], float(row[9]), float(row[10])
                except ValueError:  # keep going if there's a formatting error on one row
                    continue
                finally:
                    if state == "":  # empty values are APOs/FPOs, so skip those
                        continue

                # add the zip code to the second level of the dictionary
                try:
                    zip_code_coords_by_state[state].update({zip_code: Coordinates(lat, lon)})
                except KeyError:
                    zip_code_coords_by_state[state] = {zip_code: Coordinates(lat, lon)}

        zip_code_distances = {}  # (zip, zip) -> distance}

        # TODO: Fix this so that it works with (zip1, zip2) tuples and not strings
        for state in zip_code_coords_by_state:
            for zip_code_1, coord_1 in zip_code_coords_by_state[state].items():
                for zip_code_2, coord_2 in zip_code_coords_by_state[state].items():
                    zip_code_distances[(zip_code_1, zip_code_2)] = coord_1.distance(coord_2)

        with open(matrix_file, "wb") as file:
            pickle.dump(zip_code_distances, file)

    return zip_code_distance_matrix()


# noinspection PyUnresolvedReferences
def match_sites(list_of_sites: list, list_of_people: list) -> dict:
    """
    Returns a dictionary of People -> Sites matching TODO: criteria
    """

    return NotImplemented
