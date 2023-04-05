from django.db import models
from django.core import validators as V


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    year = models.IntegerField()
    price = models.IntegerField()
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)
