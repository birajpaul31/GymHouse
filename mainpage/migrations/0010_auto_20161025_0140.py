# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_auto_20161024_1419'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Level',
        ),
        migrations.DeleteModel(
            name='UserStatus',
        ),
    ]
