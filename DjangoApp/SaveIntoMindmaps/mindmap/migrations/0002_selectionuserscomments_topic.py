# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectionuserscomments',
            name='topic',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]