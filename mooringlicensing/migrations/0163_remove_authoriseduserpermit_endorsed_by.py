# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-21 03:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0162_numberofdaystype_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authoriseduserpermit',
            name='endorsed_by',
        ),
    ]
