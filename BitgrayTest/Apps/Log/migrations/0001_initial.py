# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'log',
            },
        ),
    ]
