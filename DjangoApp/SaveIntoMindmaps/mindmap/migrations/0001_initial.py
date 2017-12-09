# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-08 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserSelectionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comment', models.CharField(max_length=255)),
                ('parent_node', models.CharField(max_length=50)),
                ('first_saving_date', models.TimeField(auto_now_add=True)),
                ('text_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindmap.UserSelection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_authentication.UserProfileInfo')),
            ],
        ),
    ]
