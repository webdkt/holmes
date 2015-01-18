# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150109_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelog',
            name='abs_pct',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='net_pct',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='net_value',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
            preserve_default=True,
        ),
    ]
