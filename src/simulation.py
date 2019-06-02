from galaxy.planet import Planet
from galaxy.galaxy import Galaxy, PlanetsPosition


def main():
    ferengi = Planet(distance=500, speed=-1)
    betasoide = Planet(distance=2000, speed=-3)
    vulcan = Planet(distance=1000, speed=5)

    star_trek_galaxy = Galaxy([ferengi, betasoide, vulcan])

    draft_days = 0
    perfect_days = 0
    rainy_day = 0
    most_rain_day = -1
    most_rain_perimeter = 0

    for day in range(3650):
        alignment = star_trek_galaxy.planets_are_aligned(day)
        if alignment is PlanetsPosition.ALIGNED_WITH_THE_SUN:
            draft_days += 1
        elif alignment is PlanetsPosition.ALIGNED_WITH_EACHOTHER:
            perfect_days += 1
        else:
            # if we are here, planets are forming a polygon
            (sunsPosition, per) = star_trek_galaxy.calculate_suns_position(day)
            if sunsPosition is PlanetsPosition.SUN_INSIDE_POLYGON:
                rainy_day += 1
                if per > most_rain_perimeter:
                    most_rain_day = day
                    most_rain_perimeter = per

    print('Draft:', draft_days)
    print('Perfect:', perfect_days)
    print('Rainy:', rainy_day)
    print('Most rain:', most_rain_day)


if __name__ == '__main__':
    main()
