from django.db import models
from django.core import validators as V
from datetime import datetime

from apps.auto_parks.models import AutoParkModel
from core.enums.regex_enum import RegEx


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20,
                             validators=[V.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.msg)])
    year = models.IntegerField(validators=[V.MinValueValidator(1886), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(blank=True, default=1000)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)
