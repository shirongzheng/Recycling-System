# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainRecycleApp', '0009_publicrecyclingbin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idc', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pickup_info', models.TextField()),
            ],
        ),
    ]