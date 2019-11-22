from typing import NamedTuple
import numbers


class Coordinate(NamedTuple):
    latitude: numbers.Real
    longitude: numbers.Real


def generate() -> Coordinate:
    return Coordinate(latitude=-6, longitude=71.5)
