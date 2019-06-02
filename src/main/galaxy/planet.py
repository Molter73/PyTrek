from math import sin, cos


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
        return (self.distance * cos(self.speed * day),
                self.distance * sin(self.speed * day))
