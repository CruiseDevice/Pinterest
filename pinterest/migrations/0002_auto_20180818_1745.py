# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-18 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
