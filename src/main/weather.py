from peewee import *

db = PostgresqlDatabase(None)


class Weather(Model):
    date = AutoField()
    weather = CharField()

    class Meta:
        verbose_name = "weather"
        verbose_name_plural = "weathers"
        database = db

    def serialize(self):
        return {
            'day': self.date,
            'weather': self.weather,
        }

    def __str__(self):
        pass
