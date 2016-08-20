# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20160820_0236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': (('can_edit_base_profile', 'Can edit base profile'),)},
        ),
    ]
