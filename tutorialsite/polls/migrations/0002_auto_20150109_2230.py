# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=50)),
                ('share_rights', models.IntegerField()),
                ('principal', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvestPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_name', models.CharField(max_length=100)),
                ('net_value', models.DecimalField(max_digits=20, decimal_places=2)),
                ('total_share', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TradeLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trade_date', models.DateField()),
                ('a_stock_value', models.DecimalField(max_digits=20, decimal_places=2)),
                ('h_stock_value', models.DecimalField(max_digits=20, decimal_places=2)),
                ('rmb_cash_value', models.DecimalField(max_digits=20, decimal_places=2)),
                ('hkd_cash_value', models.DecimalField(max_digits=20, decimal_places=2)),
                ('hkd_rmb', models.DecimalField(max_digits=5, decimal_places=2)),
                ('index_sh', models.DecimalField(max_digits=8, decimal_places=2)),
                ('index_sz', models.DecimalField(max_digits=8, decimal_places=2)),
                ('index_zxb', models.DecimalField(max_digits=8, decimal_places=2)),
                ('index_cyb', models.DecimalField(max_digits=8, decimal_places=2)),
                ('index_sh_pct', models.DecimalField(max_digits=8, decimal_places=4)),
                ('index_sz_pct', models.DecimalField(max_digits=8, decimal_places=4)),
                ('index_zxb_pct', models.DecimalField(max_digits=8, decimal_places=4)),
                ('index_cyb_pct', models.DecimalField(max_digits=8, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='investors',
            name='invest_plan',
            field=models.ForeignKey(to='polls.InvestPlan'),
            preserve_default=True,
        ),
    ]
