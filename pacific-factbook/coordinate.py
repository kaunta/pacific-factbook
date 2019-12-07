from typing import NamedTuple
import numbers
from random import uniform


class Coordinate(NamedTuple):
    latitude: numbers.Real
    longitude: numbers.Real


def generate() -> Coordinate:
    latitude = uniform(-28.3417, -3.6754)
    longitude = uniform(153.6868, 180 + 3.6754)
    if longitude > 180:
        longitude = 180 - longitude
    return Coordinate(latitude=latitude, longitude=longitude)
