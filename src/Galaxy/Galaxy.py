from Galaxy.Planet import planet
from enum import Enum
from shapely.geometry import Point
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
    We will calculate a line from the first two planets and check the lines
    from the first planet to all others to see they are equal.
    """

    def planetsAreAligned(self, day):
        # We first calculate the slope of the two first planets
        t0 = self.planets[0].calculatePlanetPosition(day)
        t1 = self.planets[1].calculatePlanetPosition(day)

        infiniteSlope = False
        intercept = 0
        try:
            slope = (t0[0] - t1[0]) / (t0[1] - t1[1])
        except ZeroDivisionError:
            infiniteSlope = True
        else:
            intercept = t0[1] - slope * t0[0]

        for p in self.planets[2::]:
            t = p.calculatePlanetPosition(day)

            iSlope = False
            inter = 0
            try:
                s = (t0[0] - t[0]) / (t0[1] - t[1])
            except ZeroDivisionError:
                iSlope = True
            else:
                inter = t0[1] - s * t0[0]

            if iSlope is True and infiniteSlope is True:
                continue

            if s != slope or inter != intercept:
                return planetsPosition.notAligned

        if intercept is 0:
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
