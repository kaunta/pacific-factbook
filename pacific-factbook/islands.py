from typing import NamedTuple, Iterable
from functools import partial
from heapq import nsmallest

from . import coordinate
from .coordinate import Coordinate


def nearby_islands(pos: Coordinate) -> Iterable[str]:
    dist = partial(coordinate.distance, pos)
    candidates = nsmallest(3, islands, key=lambda x: dist(x.position))
    return [x.name for x in candidates]


class Island(NamedTuple):
    name: str
    position: Coordinate


def _parse(s: str) -> Coordinate:
    lat, ns, lon, ew = s.split("_")
    lat = int(lat)
    lon = int(lon)
    if ns == "S":
        lat = -lat
    if ew == "w":
        lon = -lon
    return Coordinate(latitude=lat, longitude=lon)


islands = {
    Island(name="American Samoa", position=_parse("14_S_170_W")),
    Island(name="Cook Islands", position=_parse("21_S_159_W")),
    Island(name="Easter Island", position=_parse("27_S_109_W")),
    Island(name="French Polynesia", position=_parse("17_S_149_W")),
    Island(name="Hawaii", position=_parse("21_N_157_W")),
    Island(name="New Zealand", position=_parse("42_S_173_E")),
    Island(name="Niue", position=_parse("19_S_169_W")),
    Island(name="Norfolk Island", position=_parse("29_S_167_E")),
    Island(name="Pitcairn Islands", position=_parse("25_S_130_W")),
    Island(name="Samoa", position=_parse("13_S_172_W")),
    Island(name="Tokelau", position=_parse("9_S_171_W")),
    Island(name="Tonga", position=_parse("20_S_175_W")),
    Island(name="Tuvalu", position=_parse("8_S_179_E")),
    Island(name="Wallis and Futuna", position=_parse("13_S_176_W")),
    Island(name="Rotuma", position=_parse("12_S_177_E")),
}
