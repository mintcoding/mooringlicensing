# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-15 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0081_dcvpermit_lodgement_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationtype',
            name='oracle_code_application',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
