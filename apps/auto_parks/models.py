from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_park'

    name = models.CharField(max_length=20, default='MyAutoPark',
                            validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')

    def __str__(self):
        return self.name

