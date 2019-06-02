from peewee import *

db = SqliteDatabase(None)


class Weather(Model):
    date = AutoField()
    weather = CharField()

    class Meta:
        verbose_name = "weather"
        verbose_name_plural = "weathers"
        database = db

    def __str__(self):
        pass
