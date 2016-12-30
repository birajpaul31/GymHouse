# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-30 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0025_auto_20161230_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(choices=[('8', '08:00'), ('9', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00')], default='8', max_length=5),
        ),
        migrations.AlterField(
            model_name='registration',
            name='time',
            field=models.CharField(choices=[('8', '08:00'), ('9', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00')], default='8', max_length=5),
        ),
    ]
