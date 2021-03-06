# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-29 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0038_auto_20210326_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=5, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='proposal_type',
        ),
        migrations.AlterField(
            model_name='proposal',
            name='customer_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('with_assessor', 'Under Review'), ('approved', 'Approved'), ('declined', 'Declined'), ('discarded', 'Discarded'), ('awaiting_payment', 'Awaiting Payment')], default='draft', max_length=40, verbose_name='Customer Status'),
        ),
    ]
