# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('somepain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='initialtext',
            old_name='first_name',
            new_name='txt',
        ),
        migrations.AddField(
            model_name='initialtext',
            name='offset',
            field=models.TextField(default=3, max_length=5),
            preserve_default=False,
        ),
    ]
