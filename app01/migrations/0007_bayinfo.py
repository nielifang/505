# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-15 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20190410_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='BayInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VesName', models.CharField(max_length=12)),
                ('BayId', models.CharField(max_length=12)),
            ],
        ),
    ]
