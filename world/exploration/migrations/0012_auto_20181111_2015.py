# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-11 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0009_remove_objectdb_db_player'),
        ('character', '0029_auto_20181111_2007'),
        ('exploration', '0011_shardhavenmoodfragment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShardhavenObstacle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obstacle_type', models.PositiveSmallIntegerField(choices=[(0, b'Pass a Dice Check'), (1, b'Possess a Specific Clue')])),
                ('description', models.TextField()),
                ('pass_type', models.PositiveSmallIntegerField(choices=[(0, b'Everyone must pass once'), (1, b'Everyone must pass every time'), (2, b"If anyone passes, that's enough")], default=0, verbose_name=b'Requirements')),
                ('clue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.Clue')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShardhavenObstacleRoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=40)),
                ('skill', models.CharField(max_length=40)),
                ('difficulty', models.PositiveSmallIntegerField()),
                ('target', models.PositiveSmallIntegerField()),
                ('description', models.TextField(verbose_name=b'Description Shown of this Challenge')),
                ('success_msg', models.TextField(verbose_name=b'Message to room on Success')),
                ('personal_success_msg', models.TextField(blank=True, null=True, verbose_name=b'Message to character on Success')),
                ('failure_msg', models.TextField(verbose_name=b'Message to room on Failure')),
                ('personal_failure_msg', models.TextField(blank=True, null=True, verbose_name=b'Message to character on Failure')),
                ('damage_amt', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Amount to damage a character by on failure')),
                ('damage_mit', models.BooleanField(default=True, verbose_name=b'If damage is applied, should armor mitigate it?')),
                ('damage_reason', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Short description of damage, for the damage system.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='shardhavenlayoutexit',
            name='passed_by',
            field=models.ManyToManyField(blank=True, to='objects.ObjectDB'),
        ),
        migrations.AddField(
            model_name='shardhavenobstacle',
            name='rolls',
            field=models.ManyToManyField(blank=True, to='exploration.ShardhavenObstacleRoll'),
        ),
        migrations.AddField(
            model_name='shardhavenlayoutexit',
            name='obstacle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='exploration.ShardhavenObstacle'),
        ),
    ]