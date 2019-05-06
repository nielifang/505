# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-13 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BayTierStruc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VesType', models.CharField(max_length=6)),
                ('BayNo', models.CharField(max_length=6)),
                ('TireNo', models.CharField(max_length=6)),
                ('DeckCagSig', models.BooleanField()),
                ('BayWid', models.IntegerField(null=True)),
                ('BayHigh', models.IntegerField(null=True)),
                ('CellSpeSig', models.CharField(max_length=6, null=True)),
                ('RefSig', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VesBayStruc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VesType', models.CharField(max_length=6)),
                ('BayNo', models.CharField(max_length=6)),
                ('BaySiz', models.CharField(max_length=6)),
                ('BayCom', models.CharField(max_length=6)),
                ('DeckHeg', models.IntegerField(null=True)),
                ('DeckWidMax', models.IntegerField(null=True)),
                ('CabHeg', models.IntegerField(null=True)),
                ('CabWidMax', models.IntegerField(null=True)),
                ('HatCovKind', models.CharField(max_length=6, null=True)),
                ('HatCovSiz', models.IntegerField(null=True)),
                ('BayX', models.IntegerField(null=True)),
                ('BayY', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VesExpSto',
            fields=[
                ('Vessel', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('Voyage', models.CharField(max_length=20, unique=True)),
                ('VesCellNo', models.CharField(max_length=20, null=True)),
                ('ColNo', models.IntegerField(null=True)),
                ('DeckCagSig', models.CharField(max_length=20, null=True)),
                ('CtnNo', models.CharField(max_length=20, null=True)),
                ('CtnTyp', models.CharField(max_length=20, null=True)),
                ('Size', models.CharField(max_length=20, null=True)),
                ('Status', models.CharField(max_length=20, null=True)),
                ('CtnWegt', models.IntegerField(null=True)),
                ('GForce', models.CharField(max_length=20, null=True)),
                ('StaPort', models.CharField(max_length=20, null=True)),
                ('UnloadPort', models.CharField(max_length=20, null=True)),
                ('DesPort', models.CharField(max_length=20, null=True)),
                ('CtnOpeSta', models.CharField(max_length=20, null=True)),
                ('PlaCtnCel', models.CharField(max_length=20, null=True)),
                ('YardCel', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VesImpSto',
            fields=[
                ('Vessel', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('Voyage', models.CharField(max_length=20, unique=True)),
                ('VesCellNo', models.CharField(max_length=20, null=True)),
                ('ColNo', models.IntegerField(null=True)),
                ('DeckCagSig', models.CharField(max_length=20, null=True)),
                ('CtnNo', models.CharField(max_length=20, null=True)),
                ('CtnTyp', models.CharField(max_length=20, null=True)),
                ('Size', models.CharField(max_length=20, null=True)),
                ('Status', models.CharField(max_length=20, null=True)),
                ('CtnWegt', models.IntegerField(null=True)),
                ('Owner', models.CharField(max_length=20, null=True)),
                ('GForce', models.CharField(max_length=20, null=True)),
                ('StaPort', models.CharField(max_length=20, null=True)),
                ('UnloadPort', models.CharField(max_length=20, null=True)),
                ('DesPort', models.CharField(max_length=20, null=True)),
                ('StrPickAwayCtn', models.CharField(max_length=20, null=True)),
                ('CtnOpeSta', models.CharField(max_length=20, null=True)),
                ('PlaCtnCel', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VesStruc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VesType', models.CharField(max_length=6)),
                ('VesLeng', models.IntegerField()),
                ('VesWidth', models.IntegerField()),
                ('VesFrLeng', models.IntegerField()),
                ('TweBayNum', models.IntegerField()),
                ('FotBayNum', models.IntegerField()),
                ('FotBayCom', models.CharField(max_length=32, null=True)),
                ('EngRomPos', models.IntegerField(null=True)),
                ('EngRomWid', models.IntegerField(null=True)),
                ('MidBayDeaWit', models.BooleanField()),
                ('RefCtnCap', models.FloatField(null=True)),
                ('VesEntBerSpd', models.CharField(max_length=18, null=True)),
                ('VesBerSpd', models.CharField(max_length=18, null=True)),
                ('HigCtnCap', models.FloatField(null=True)),
                ('CapCtnFotFiv', models.FloatField(null=True)),
                ('VesEmpGrvHeg', models.CharField(max_length=10, null=True)),
                ('VesAtt', models.CharField(max_length=10, null=True)),
                ('LoadWeigth', models.IntegerField(null=True)),
                ('DeckCapWegt', models.IntegerField(null=True)),
                ('CabCap', models.IntegerField(null=True)),
                ('DanCtnAlw', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='VesVoyageInfo',
            fields=[
                ('Vessel', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('ImpVoy', models.CharField(max_length=32)),
                ('ExpVoy', models.CharField(max_length=32)),
                ('VesType', models.CharField(max_length=12)),
                ('PlaBerThgTim', models.DateTimeField(auto_now_add=True, null=True)),
                ('PlaUnbThgTim', models.DateTimeField(auto_now_add=True, null=True)),
                ('ReaBerThgTim', models.DateTimeField(auto_now_add=True, null=True)),
                ('ActUnbTim', models.DateTimeField(auto_now_add=True, null=True)),
                ('PlaBerThgPos', models.IntegerField(null=True)),
                ('ActBerPos', models.IntegerField(null=True)),
                ('BerThgDir', models.CharField(max_length=4, null=True)),
                ('VesDrauMax', models.FloatField(null=True)),
                ('PlaClosCustTim', models.DateTimeField(auto_now_add=True, null=True)),
                ('ClosCustTim', models.DateTimeField(auto_now_add=True, null=True)),
                ('OpAssSign', models.CharField(max_length=12, null=True)),
                ('EntPlanMakSig', models.CharField(max_length=32, null=True)),
                ('TaskFiniSig', models.BooleanField()),
                ('UnBSta', models.NullBooleanField()),
            ],
        ),
    ]