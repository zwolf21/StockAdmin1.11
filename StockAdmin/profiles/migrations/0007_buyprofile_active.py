# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20171107_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyprofile',
            name='active',
            field=models.BooleanField(default=True, verbose_name='사용중'),
        ),
    ]
