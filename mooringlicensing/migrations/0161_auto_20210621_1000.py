# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-21 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0160_auto_20210618_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberofdayssetting',
            name='number_of_days_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='mooringlicensing.NumberOfDaysType'),
        ),
    ]
