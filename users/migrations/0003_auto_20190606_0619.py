# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-06 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190606_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Resident', 'Resident')], default='Resident', max_length=10),
        ),
    ]
