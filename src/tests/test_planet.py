from main.galaxy.planet import Planet
from math import cos, sin, radians


class TestPlanet(object):
    def test_calculate_planet_position(self):
        planet = Planet(distance=1, speed=90)
        for day in range(4):
            assert (
                round(cos(radians(90 * day)), 2),
                round(sin(radians(90 * day)), 2)
            ) == planet.calculate_planet_position(day)
