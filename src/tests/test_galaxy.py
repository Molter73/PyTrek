from main.galaxy.planet import Planet
from main.galaxy.galaxy import Galaxy, PlanetsPosition


class TestGalaxy(object):
    def test_planets_are_aligned(self):
        galaxy = Galaxy([
            Planet(distance=1, speed=0),
            Planet(distance=2, speed=90)])

        assert galaxy.planets_are_aligned(
            1) == PlanetsPosition.ALIGNED_WITH_EACHOTHER
        assert galaxy.planets_are_aligned(
            2) == PlanetsPosition.ALIGNED_WITH_THE_SUN

        galaxy = Galaxy([
            Planet(distance=1, speed=0),
            Planet(distance=2, speed=45),
            Planet(distance=2, speed=90)])
        assert galaxy.planets_are_aligned(1) == PlanetsPosition.NOT_ALIGNED

    def test_calculate_suns_position(self):
        galaxy = Galaxy([
            Planet(distance=1, speed=0),
            Planet(distance=2, speed=45),
            Planet(distance=2, speed=90)])

        assert galaxy.calculate_suns_position(
            1)[0] == PlanetsPosition.SUN_NOT_INSIDE_POLYGON
        assert galaxy.calculate_suns_position(
            3)[0] == PlanetsPosition.SUN_INSIDE_POLYGON

    def test_constructor(self):
        first_planet = Planet(distance=1, speed=0)
        second_planet = Planet(distance=2, speed=90)
        galaxy = Galaxy([first_planet, second_planet])

        assert galaxy.planets == [first_planet, second_planet]
