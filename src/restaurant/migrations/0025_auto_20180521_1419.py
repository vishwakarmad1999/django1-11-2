# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-21 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import restaurant.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0024_auto_20180521_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=120, validators=[restaurant.validators.validate_dish_name]),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='name',
            field=models.CharField(max_length=120, validators=[restaurant.validators.validate_rl_name]),
        ),
    ]
