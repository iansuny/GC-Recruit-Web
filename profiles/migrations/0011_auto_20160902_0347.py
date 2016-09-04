# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-02 03:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20160902_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='student',
            field=models.ManyToManyField(to='profiles.Student'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
