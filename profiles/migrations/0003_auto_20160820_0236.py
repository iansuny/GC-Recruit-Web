# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160820_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='badge',
            field=models.ForeignKey(to='profiles.Badge', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='follow',
            field=models.ForeignKey(to='profiles.Follow', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='talent',
            field=models.ForeignKey(to='profiles.Talent', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='team',
            field=models.ForeignKey(to='profiles.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='interest',
            field=models.ForeignKey(to='profiles.Interest', null=True),
            preserve_default=True,
        ),
    ]
