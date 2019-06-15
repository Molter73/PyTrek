from weather import db, Weather
from galaxy import Galaxy, PlanetsPosition
from planet import Planet
import json, os

def main():
    # Initialize the db
    db_config = {}
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\db-config.json") as db_config_file:
        db_config = json.load(db_config_file)
    db.init(db_config['db-name'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port'])
    db.connect()
    tables = db.get_tables()
    if 'Weather' in tables:
        db.drop_tables(Weather)
    db.create_tables([Weather])

    # Create the galaxy we are gonna store
    ferengi = Planet(distance=500, speed=-1)
    betasoide = Planet(distance=2000, speed=-3)
    vulcan = Planet(distance=1000, speed=5)

    star_trek_galaxy = Galaxy([ferengi, betasoide, vulcan])
    weather = {}

    with db.atomic():
        for day in range(3650):
            weather['day'] = day
            alignment = star_trek_galaxy.planets_are_aligned(day)
            if alignment is PlanetsPosition.ALIGNED_WITH_THE_SUN:
                weather['weather'] = 'draft'
            elif alignment is PlanetsPosition.ALIGNED_WITH_EACHOTHER:
                weather['weather'] = 'perfect'
            else:
                # if we are here, planets are forming a polygon
                (sunsPosition, per) = star_trek_galaxy.calculate_suns_position(day)
                if sunsPosition is PlanetsPosition.SUN_INSIDE_POLYGON:
                    weather['weather'] = 'rain'
                else:
                    weather['weather'] = 'sunny'
            Weather.create(**weather)


if __name__ == '__main__':
    main()
