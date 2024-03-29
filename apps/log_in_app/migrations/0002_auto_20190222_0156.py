# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-22 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_in_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='log_in_app.users')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='messages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='log_in_app.messages'),
        ),
    ]
