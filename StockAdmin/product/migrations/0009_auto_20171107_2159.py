# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20171107_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='std_price',
            field=models.DecimalField(decimal_places=2, max_digits=100, verbose_name='표준가격'),
        ),
    ]
