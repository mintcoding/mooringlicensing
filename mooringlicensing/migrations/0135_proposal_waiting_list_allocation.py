# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-02 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0134_proposal_allocated_mooring'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='waiting_list_allocation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ria_generated_proposal', to='mooringlicensing.Approval'),
        ),
    ]
