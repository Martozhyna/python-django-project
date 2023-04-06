from django.db import models
from django.core import validators as V

from apps.auto_parks.models import AutoParksModel

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    year = models.IntegerField()
    price = models.IntegerField()
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)
