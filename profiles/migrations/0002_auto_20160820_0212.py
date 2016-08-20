# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'student1', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'ntu', max_length=50)),
                ('need', models.IntegerField(max_length=5)),
                ('interest', models.ForeignKey(to='profiles.Interest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='student',
            name='badge',
        ),
        migrations.RemoveField(
            model_name='student',
            name='talent',
        ),
        migrations.AlterField(
            model_name='badge',
            name='name',
            field=models.CharField(default=b'beginner', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interest',
            name='name',
            field=models.CharField(default=b'Medical Health', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='talent',
            name='name',
            field=models.CharField(default=b'Math', max_length=50),
            preserve_default=True,
        ),
    ]
