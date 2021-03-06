# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-20 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModPy', '0003_module_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='frontend',
        ),
        migrations.RemoveField(
            model_name='module',
            name='logic',
        ),
        migrations.AddField(
            model_name='module',
            name='InputDescription',
            field=models.TextField(default='Some description'),
        ),
        migrations.AddField(
            model_name='module',
            name='InputType',
            field=models.TextField(default='Some type'),
        ),
        migrations.AddField(
            model_name='module',
            name='NumberOfInputs',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='SubstitutedCode',
            field=models.TextField(default='Some code'),
        ),
        migrations.AddField(
            model_name='module',
            name='developer',
            field=models.CharField(default='Codevisor Team', max_length=150),
        ),
        migrations.AddField(
            model_name='module',
            name='languages',
            field=models.TextField(default='Python'),
        ),
    ]
