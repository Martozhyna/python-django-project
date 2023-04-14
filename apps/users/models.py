from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True, validators=[V.MinLengthValidator(6)])
    password = models.CharField(max_length=128,
                                validators=[V.RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20, default='John',
                            validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    surname = models.CharField(max_length=20, default='Doe',
                               validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    age = models.IntegerField(validators=[V.MinValueValidator(14), ])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
