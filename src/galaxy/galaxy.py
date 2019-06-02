from Galaxy.Planet import planet
from enum import Enum
from shapely.geometry import Point, LineString
from shapely.geometry.polygon import Polygon


class planetsPosition(Enum):
    notAligned = 0
    alignedWithEachother = 1
    alignedWithTheSun = 2
    sunInsidePolygon = 3
    sunNotInsidePolygon = 4


class galaxy:
    planets = []

    def __init__(self, planets=[]):
        self.planets = planets

    """
    We need to check if all planets in this galaxy are in a straight line
    We will calculate a line from the first two planets and to see if all
    others are inside of it.
    """

    def planetsAreAligned(self, day):
        line = LineString([self.planets[0].calculatePlanetPosition(
            day), self.planets[1].calculatePlanetPosition(day)])

        for p in self.planets[2::]:
            if not line.within(Point(p.calculatePlanetPosition(day))):
                return planetsPosition.notAligned

        if line.within(Point(0, 0)):
            return planetsPosition.alignedWithTheSun
        return planetsPosition.alignedWithEachother

    """
    This method will be responsible for creating a polygon with all the
    galaxy's planets and determining whether the sun is inside of it
    If the sun is inside, also returns the polygons perimeter
    """

    def calculateSunsPosition(self, day):
        positions = []
        for p in self.planets:
            positions.append(p.calculatePlanetPosition(day))

        poly = Polygon(positions)

        if poly.contains(Point(0, 0)):
            return (planetsPosition.sunInsidePolygon, poly.length)
        return (planetsPosition.sunNotInsidePolygon, poly.length)
