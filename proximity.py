import csv
import numpy as np
from dataclasses import dataclass
from math import radians, sqrt, sin, cos, asin
from os import path
from user_input import Person
from aggregator import Site


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


def zip_code_distance_matrix_ny() -> np.array:
    """Returns a numpy array where [zip - 10000][zip - 10000] = distance:float for all zip codes in NY"""

    matrix_file = "res/ZipCodeMatrixNY.npy"

    # if the array exists, load it into memory and return it
    if path.exists(matrix_file):
        distance_matrix = np.load(matrix_file)
    # otherwise, create it, write it and return it
    else:
        # build a zip -> coord dictionary
        zip_code_coordinates = {}

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

                # only add values for NY currently
                if state == "NY":
                    zip_code_coordinates[zip_code] = Coordinates(lat, lon)

        # create zip1 x zip2 = distance matrix
        # zip codes in NY range from 10000 to 14999, so subtract 10000 from the zip code to match it to its index
        distance_matrix = np.zeros((5000, 5000), dtype=np.float64)
        for zip1, coord1 in zip_code_coordinates.items():
            for zip2, coord2 in zip_code_coordinates.items():
                # skip special government zipcodes that are out of range
                if zip1 not in range(10000, 15000) or zip2 not in range(10000, 15000):
                    continue
                else:
                    array_zip1 = zip1 - 10000
                    array_zip2 = zip2 - 10000

                # distance is the same in either direction, so avoid recomputing if possible
                if distance_matrix[array_zip2][array_zip1]:
                    distance_matrix[array_zip1][array_zip2] = distance_matrix[array_zip2][array_zip1]
                # otherwise, compute the distance between the zips and add it to the dictionary
                else:
                    distance_matrix[array_zip1][array_zip2] = coord1.distance(coord2)

        # # create dictionary to store (zip1, zip2) -> distance pairs
        # zip_code_distances = {}
        #
        # # generate (zip1, zip2) -> distance tuple pairs
        # for zip1, coord1 in zip_code_coordinates.items():
        #     for zip2, coord2 in zip_code_coordinates.items():
        #         # distance is the same in either direction, so avoid recomputing it if possible
        #         if (zip2, zip1) in zip_code_distances:
        #             zip_code_distances[(zip1, zip2)] = zip_code_distances[(zip2, zip1)]
        #         # otherwise, compute the distance between the zips and add it to the dictionary
        #         else:
        #             zip_code_distances[(zip1, zip2)] = coord1.distance(coord2)

        # write the dictionary to disk to avoid recomputing it later
        np.save(matrix_file, distance_matrix)

    return distance_matrix


def match_sites(list_of_sites: list[Site], list_of_people: list[Person]) -> dict:
    """Returns a dictionary of People -> Sites with availability in specified radius"""

    distance_matrix = zip_code_distance_matrix_ny()

    return NotImplemented
