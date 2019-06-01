from Galaxy.Planet import planet
from Galaxy.Galaxy import galaxy, planetsAligned


def main():
    Ferengi = planet(distance=500, speed=-1)
    Betasoide = planet(distance=2000, speed=-3)
    Vulcan = planet(distance=1000, speed=5)

    StarTrekGalaxy = galaxy([Ferengi, Betasoide, Vulcan])

    draftDays = 0
    perfectDays = 0

    for day in range(3650):
        alignment = StarTrekGalaxy.planetsAreAligned(day)
        if alignment is planetsAligned.alignedWithTheSun:
            draftDays += 1
        elif alignment is planetsAligned.alignedWithEachother:
            perfectDays += 1

    print('Draft:', draftDays)
    print('Perfect:', perfectDays)


if __name__ == '__main__':
    main()
