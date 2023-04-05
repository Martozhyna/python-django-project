from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20)
    year = models.IntegerField()
    seat = models.IntegerField()
    basket = models.CharField(max_length=20)
    engine = models.FloatField()
