# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20161024_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_id',
        ),
    ]
