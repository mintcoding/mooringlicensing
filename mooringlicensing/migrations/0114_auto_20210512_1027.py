# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-12 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0113_auto_20210511_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='company_ownership_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
