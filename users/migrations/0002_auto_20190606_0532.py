# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-06 02:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoods.Hoods'),
        ),
    ]