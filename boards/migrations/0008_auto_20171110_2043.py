# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0007_auto_20171109_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
