# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_markets'),
        ('profiles', '0003_auto_20171107_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyprofile',
            name='markets',
        ),
        migrations.AddField(
            model_name='buyprofile',
            name='market',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Market'),
        ),
        migrations.AlterField(
            model_name='buyprofile',
            name='box_amount',
            field=models.IntegerField(default=1, null=True, verbose_name='묶음수량'),
        ),
    ]