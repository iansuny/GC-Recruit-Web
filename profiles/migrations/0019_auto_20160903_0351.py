# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-03 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20160903_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='follow',
            field=models.ManyToManyField(null=True, related_name='_student_follow_+', to='profiles.Student'),
        ),
    ]