# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-24 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20190423_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baystruc',
            name='HatCovKind',
            field=models.CharField(max_length=60, null=True, verbose_name='舱盖板'),
        ),
    ]
