from Galaxy.Planet import planet
from Galaxy.Galaxy import galaxy, planetsPosition


def main():
    Ferengi = planet(distance=500, speed=-1)
    Betasoide = planet(distance=2000, speed=-3)
    Vulcan = planet(distance=1000, speed=5)

    StarTrekGalaxy = galaxy([Ferengi, Betasoide, Vulcan])

    draftDays = 0
    perfectDays = 0
    rainyDay = 0
    mostRainDay = -1
    mostRainPerimeter = 0

    for day in range(3650):
        alignment = StarTrekGalaxy.planetsAreAligned(day)
        if alignment is planetsPosition.alignedWithTheSun:
            draftDays += 1
        elif alignment is planetsPosition.alignedWithEachother:
            perfectDays += 1
        else:
            # if we are here, planets are forming a polygon
            (sunsPosition, per) = StarTrekGalaxy.calculateSunsPosition(day)
            if sunsPosition is planetsPosition.sunInsidePolygon:
                rainyDay += 1
                if per > mostRainPerimeter:
                    mostRainDay = day

    print('Draft:', draftDays)
    print('Perfect:', perfectDays)
    print('Rainy:', rainyDay)
    print('Most rain:', mostRainDay)

if __name__ == '__main__':
    main()
