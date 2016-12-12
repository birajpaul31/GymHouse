# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-12 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import mainpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0019_profile_registrations'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='heart_rate',
            field=models.IntegerField(blank=True, help_text='Please enter your resting heart rate', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=mainpage.models.get_user_path),
        ),
    ]