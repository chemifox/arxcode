# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-26 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0002_auto_20190503_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effecttrigger',
            name='conditional_check',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Prestige Rank'), (1, 'Prestige Value'), (4, 'Org Name and Rank Range'), (5, 'Current Health %'), (6, 'Change Amount')], default=0),
        ),
    ]