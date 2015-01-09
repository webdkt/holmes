# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150109_2230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Investors',
            new_name='Investor',
        ),
        migrations.RenameField(
            model_name='investor',
            old_name='invest_plan',
            new_name='investplan',
        ),
        migrations.AddField(
            model_name='tradelog',
            name='investplan',
            field=models.ForeignKey(default=1, to='polls.InvestPlan'),
            preserve_default=False,
        ),
    ]
