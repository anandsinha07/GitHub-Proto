# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-11 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_profile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]