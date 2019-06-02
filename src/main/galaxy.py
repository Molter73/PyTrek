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

    def planets_are_aligned(self, day):
        """
        We need to check if all planets in this galaxy are in a straight line
        We will calculate a line from the first two planets and see if all
        others are inside of it.
        """
        line = LineString([self.planets[0].calculate_planet_position(
            day), self.planets[1].calculate_planet_position(day)])

        for p in self.planets[2::]:
            if not line.contains(Point(p.calculate_planet_position(day))):
                return PlanetsPosition.NOT_ALIGNED

        if line.contains(Point(0, 0)):
            return PlanetsPosition.ALIGNED_WITH_THE_SUN
        return PlanetsPosition.ALIGNED_WITH_EACHOTHER

    def calculate_suns_position(self, day):
        """
        This method will be responsible for creating a polygon with all the
        galaxy's planets and determining whether the sun is inside of it
        If the sun is inside, also returns the polygons perimeter
        """
        positions = []
        for p in self.planets:
            positions.append(p.calculate_planet_position(day))

        poly = Polygon(positions)

        if poly.contains(Point(0, 0)):
            return (PlanetsPosition.SUN_INSIDE_POLYGON, poly.length)
        return (PlanetsPosition.SUN_NOT_INSIDE_POLYGON, poly.length)
