# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-03 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0135_proposal_waiting_list_allocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='status',
            field=models.CharField(choices=[('current', 'Current'), ('expired', 'Expired'), ('cancelled', 'Cancelled'), ('surrendered', 'Surrendered'), ('suspended', 'Suspended'), ('extended', 'Extended'), ('awaiting_payment', 'Awaiting Payment'), ('offered', 'Mooring Licence offered'), ('approved', 'Mooring Licence approved')], default='current', max_length=40),
        ),
    ]
