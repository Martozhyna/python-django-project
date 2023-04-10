from django.db import models
from django.core import validators as V

from apps.auto_parks.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20,
                             validators=[V.RegexValidator(r'^([A-Z][A-Za-z]{1,19})$')])
    year = models.IntegerField(validators=[V.MinValueValidator(1886), V.MaxValueValidator(2023)])
    price = models.IntegerField(blank=True, default=1000)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)
