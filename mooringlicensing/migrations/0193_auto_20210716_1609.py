# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-16 08:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0192_auto_20210715_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposalapprovergroup',
            name='members',
        ),
        migrations.RemoveField(
            model_name='proposalassessorgroup',
            name='members',
        ),
        migrations.DeleteModel(
            name='ProposalApproverGroup',
        ),
        migrations.DeleteModel(
            name='ProposalAssessorGroup',
        ),
    ]
