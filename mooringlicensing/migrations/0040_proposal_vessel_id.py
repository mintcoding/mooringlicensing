# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-30 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0039_proposal_rego_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='vessel_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
