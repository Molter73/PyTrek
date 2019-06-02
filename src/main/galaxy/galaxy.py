from enum import Enum
from shapely.geometry import Point, LineString
from shapely.geometry.polygon import Polygon


class PlanetsPosition(Enum):
    NOT_ALIGNED = 0
    ALIGNED_WITH_EACHOTHER = 1
    ALIGNED_WITH_THE_SUN = 2
    SUN_INSIDE_POLYGON = 3
    SUN_NOT_INSIDE_POLYGON = 4


class Galaxy:
    planets = []

    def __init__(self, planets=[]):
        self.planets = planets

    """
    We need to check if all planets in this galaxy are in a straight line
    We will calculate a line from the first two planets and to see if all
    others are inside of it.
    """

    def planets_are_aligned(self, day):
        line = LineString([self.planets[0].calculate_planet_position(
            day), self.planets[1].calculate_planet_position(day)])

        for p in self.planets[2::]:
            if not line.within(Point(p.calculate_planet_position(day))):
                return PlanetsPosition.NOT_ALIGNED

        if line.within(Point(0, 0)):
            return PlanetsPosition.ALIGNED_WITH_THE_SUN
        return PlanetsPosition.ALIGNED_WITH_EACHOTHER

    """
    This method will be responsible for creating a polygon with all the
    galaxy's planets and determining whether the sun is inside of it
    If the sun is inside, also returns the polygons perimeter
    """

    def calculate_suns_position(self, day):
        positions = []
        for p in self.planets:
            positions.append(p.calculate_planet_position(day))

        poly = Polygon(positions)

        if poly.contains(Point(0, 0)):
            return (PlanetsPosition.SUN_INSIDE_POLYGON, poly.length)
        return (PlanetsPosition.SUN_NOT_INSIDE_POLYGON, poly.length)
