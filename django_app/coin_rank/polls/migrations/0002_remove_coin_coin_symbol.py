# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 00:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='coin_symbol',
        ),
    ]
