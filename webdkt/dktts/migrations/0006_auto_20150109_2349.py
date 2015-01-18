# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150109_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='investplan',
            name='begin_value',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tradelog',
            name='abs_pct',
            field=models.DecimalField(default=1, max_digits=8, decimal_places=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tradelog',
            name='net_change',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tradelog',
            name='net_pct',
            field=models.DecimalField(default=1, max_digits=8, decimal_places=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tradelog',
            name='net_value',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='index_cyb',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='index_cyb_pct',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='index_sh',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='index_sh_pct',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='index_sz',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='index_sz_pct',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='index_zxb',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='index_zxb_pct',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=4),
            preserve_default=True,
        ),
    ]
