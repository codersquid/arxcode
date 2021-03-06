# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0009_remove_objectdb_db_player'),
        ('exploration', '0032_shardhavenlayoutexit_override'),
    ]

    operations = [
        migrations.AddField(
            model_name='shardhavenlayoutsquare',
            name='last_visited',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shardhavenlayoutsquare',
            name='visitors',
            field=models.ManyToManyField(related_name='_shardhavenlayoutsquare_visitors_+', to='objects.ObjectDB'),
        ),
    ]
