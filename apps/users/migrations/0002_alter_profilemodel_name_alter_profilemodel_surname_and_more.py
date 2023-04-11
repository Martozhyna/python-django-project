# Generated by Django 4.2 on 2023-04-11 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(default='John', max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,20}$', 'only letters min 2 max 20 ch')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(default='Doe', max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,20}$', 'only letters min 2 max 20 ch')]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\s])[^\\s]{8,20}$', ['password must contain 1 number (0-9)', 'password must contain 1 uppercase letter', 'password must contain 1 lowercase letter', 'password must contain 1 non-alpha numeric', 'password min 8 max 20 ch'])]),
        ),
    ]
