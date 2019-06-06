# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-06 06:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hoods', '0002_hoods_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
