# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-15 02:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mooringlicensing', '0076_auto_20210415_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcvpermit',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mooringlicensing_dcv_permits', to=settings.AUTH_USER_MODEL),
        ),
    ]
