# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-06 10:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0003_remove_pin_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='pin',
            name='users_like',
            field=models.ManyToManyField(blank=True, default='', related_name='pins_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
