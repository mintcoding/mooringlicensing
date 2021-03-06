# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-11 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0149_auto_20210610_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='customer_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('with_assessor', 'Under Review'), ('awaiting_endorsement', 'Awaiting Endorsement'), ('awaiting_documents', 'Awaiting Documents'), ('printing_sticker', 'Printing Sticker'), ('approved', 'Approved'), ('declined', 'Declined'), ('discarded', 'Discarded'), ('awaiting_payment', 'Awaiting Payment'), ('awaiting_payment_sticker_returned', 'Awaiting Payment and Sticker Returned'), ('awaiting_sticker_returned', 'Awaiting Sticker Returned')], default='draft', max_length=40, verbose_name='Customer Status'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='processing_status',
            field=models.CharField(choices=[('temp', 'Temporary'), ('draft', 'Draft'), ('with_assessor', 'With Assessor'), ('with_assessor_requirements', 'With Assessor (Requirements)'), ('with_approver', 'With Approver'), ('renewal', 'Renewal'), ('licence_amendment', 'Licence Amendment'), ('awaiting_applicant_respone', 'Awaiting Applicant Response'), ('awaiting_assessor_response', 'Awaiting Assessor Response'), ('printing_sticker', 'Printing Sticker'), ('awaiting_endorsement', 'Awaiting Endorsement'), ('awaiting_documents', 'Awaiting Documents'), ('approved', 'Approved'), ('declined', 'Declined'), ('discarded', 'Discarded'), ('awaiting_payment', 'Awaiting Payment'), ('awaiting_payment_sticker_returned', 'Awaiting Payment and Sticker Returned'), ('awaiting_sticker_returned', 'Awaiting Sticker Returned')], default='draft', max_length=30, verbose_name='Processing Status'),
        ),
    ]
