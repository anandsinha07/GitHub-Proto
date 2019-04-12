# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-11 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0011_auto_20180611_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, default='Not provided', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='Not provided', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, default='Not provided', max_length=120, null=True),
        ),
    ]