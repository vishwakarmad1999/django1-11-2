# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_remove_restaurantlocation_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
