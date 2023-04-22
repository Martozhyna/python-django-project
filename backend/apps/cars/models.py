from datetime import datetime

from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.uppload_car_services import upload_to

from apps.auto_parks.models import AutoParkModel

from .managers import CarManager


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    model = models.CharField(max_length=20,
                             validators=[V.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.msg)])
    year = models.IntegerField(validators=[V.MinValueValidator(1886), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(blank=True, default=1000)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)

    objects = CarManager.as_manager()

    def __repr__(self):
        return str(self.__dict__)


class CarPhotoModel(models.Model):
    class Meta:
        db_table = 'cars_photo'

    photo = models.ImageField(upload_to=upload_to, blank=True)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='photos')
