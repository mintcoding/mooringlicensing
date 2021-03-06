# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-30 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0183_auto_20210629_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='status',
            field=models.CharField(choices=[('ready', 'Ready'), ('printing', 'Printing'), ('current', 'Current'), ('to_be_returned', 'To be Returned'), ('returned', 'Returned'), ('lost', 'Lost'), ('expired', 'Expired'), ('cancelled', 'Cancelled')], default='ready', max_length=40),
        ),
    ]
