# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-13 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0013_programs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Programs',
            new_name='Program',
        ),
    ]
