# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-25 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0032_auto_20210325_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='org_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='proposal',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=5),
        ),
    ]
