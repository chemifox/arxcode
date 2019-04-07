# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-03 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effecttrigger',
            name='conditional_check',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Prestige Rank'), (1, 'Prestige Value'), (4, 'Org Name and Rank Range'), (5, 'Current Health %'), (6, 'Change Amount')], default=0),
        ),
    ]
