# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-13 08:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0015_program_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
