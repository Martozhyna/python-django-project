from django.db import models
from django.core import validators as V

from apps.users.models import UserModel


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_park'

    name = models.CharField(max_length=30, default='MyAutoPark',
                            validators=[V.RegexValidator(r'^([A-Z][A-Za-z\d])$')])
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
