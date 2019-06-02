from math import sin, cos, radians


class Planet:
    distance = 0
    speed = 0

    def __init__(self, distance=0, speed=0):
        self.distance = distance
        self.speed = speed

    """
    Returns an (X,Y) pair, describing the planets position at a given day
    """

    def calculate_planet_position(self, day=0):
        return (
            round(self.distance * cos(radians(self.speed * day)), 2),
            round(self.distance * sin(radians(self.speed * day)), 2))
