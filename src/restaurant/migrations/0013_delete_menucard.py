# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_menucard'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MenuCard',
        ),
    ]
