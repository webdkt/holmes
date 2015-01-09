# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150109_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investor',
            old_name='investplan',
            new_name='invest_plan',
        ),
        migrations.RenameField(
            model_name='tradelog',
            old_name='investplan',
            new_name='invest_plan',
        ),
    ]
