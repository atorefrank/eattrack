# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='fbid',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
