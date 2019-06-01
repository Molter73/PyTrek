from math import sin, cos


class planet:
    distance = 0
    speed = 0

    def __init__(self, distance=0, speed=0):
        self.distance = distance
        self.speed = speed

    """
    Returns an (X,Y) pair, describing the planets position at a given day
    """

    def calculatePlanetPosition(self, day=0):
        return (self.distance * cos(self.speed * day),
                self.distance * sin(self.speed * day))
