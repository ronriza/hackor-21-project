from dataclasses import dataclass
from numpy import array
from math import radians, sqrt, sin, cos, asin


@dataclass(frozen=True)
class ZipCode:
    """Represents a zip code with a value and latitude & longitude horizontal coordinates"""
    _value: int  # zip code in 5-digit format
    _lat: float
    _lon: float

    @property
    def lat(self) -> float:
        return self._lat

    @property
    def lon(self) -> float:
        return self._lon

    @property
    def value(self) -> int:
        return self._value

    def distance_from(self, other):
        """Returns the distance in miles between this pair of coordinates and another pair of coordinates"""
        if not isinstance(other, ZipCode):
            return NotImplemented
        else:
            # return the great circle distance between the two zip codes' coordinates in miles
            raise NotImplementedError


# noinspection PyUnresolvedReferences
def match_sites(list_of_sites: list[Site], list_of_people: list[Person]) -> dict:
    """
    Returns a dictionary of People -> Sites matching TODO: criteria
    """

    return dict()
