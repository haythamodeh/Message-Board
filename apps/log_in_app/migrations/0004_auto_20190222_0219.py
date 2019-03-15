# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-22 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_in_app', '0003_auto_20190222_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='messages',
            field=models.ManyToManyField(related_name='messages', to='log_in_app.Messages'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='users',
            field=models.ManyToManyField(related_name='users', to='log_in_app.Users'),
        ),
    ]
