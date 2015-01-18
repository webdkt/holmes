# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150109_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tradelog',
            old_name='hkd_cash_value',
            new_name='hkd_total_value',
        ),
        migrations.RenameField(
            model_name='tradelog',
            old_name='rmb_cash_value',
            new_name='rmb_total_value',
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='hkd_rmb',
            field=models.DecimalField(default=0.8, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
