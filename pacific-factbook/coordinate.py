from random import uniform
from typing import NamedTuple
import math
import numbers


class Coordinate(NamedTuple):
    latitude: numbers.Real
    longitude: numbers.Real


def distance(p1: Coordinate, p2: Coordinate) -> numbers.Real:
    # FIXME
    return math.sqrt(
        (p1.latitude - p2.latitude) ** 2 + (p1.longitude - p2.longitude) ** 2
    )


def generate() -> Coordinate:
    latitude = uniform(-28.3417, -3.6754)
    longitude = uniform(153.6868, 180 + 3.6754)
    if longitude > 180:
        longitude = 180 - longitude
    return Coordinate(latitude=latitude, longitude=longitude)
