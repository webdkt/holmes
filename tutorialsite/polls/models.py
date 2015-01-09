# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Max
from decimal import *

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):              # __unicode__ on Python 2
		return self.question_text
		
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unicode__(self):              # __unicode__ on Python 2
		return self.choice_text
		
		

	
class InvestPlan(models.Model):
	plan_name = models.CharField(max_length=100)
	net_value = models.DecimalField(max_digits=20,decimal_places=2)
	total_share = models.IntegerField() #权益总额
	net_value = models.DecimalField(max_digits=20,decimal_places=2)
	begin_value = models.DecimalField(max_digits=20,decimal_places=2)
	def __unicode__(self):              # __unicode__ on Python 2
		return self.plan_name

class Investor(models.Model):
	full_name = models.CharField(max_length=50)  #姓名
	share_rights = models.IntegerField() #权益分额
	principal = models.DecimalField(max_digits=20,decimal_places=2)  #本金金额
	invest_plan = models.ForeignKey(InvestPlan)	
	def __unicode__(self):              # __unicode__ on Python 2
		return self.full_name
	
	def net_value(self):
		plan = self.invest_plan
		return (plan.net_value * (Decimal(self.share_rights)/Decimal(plan.total_share))).quantize(Decimal('.01'), rounding=ROUND_DOWN)
	
class TradeLog(models.Model):
	invest_plan = models.ForeignKey(InvestPlan)
	trade_date = models.DateField()
	a_stock_value = models.DecimalField(max_digits=20,decimal_places=2)
	h_stock_value = models.DecimalField(max_digits=20,decimal_places=2)
	rmb_total_value = models.DecimalField(max_digits=20,decimal_places=2)
	hkd_total_value = models.DecimalField(max_digits=20,decimal_places=2)
	hkd_rmb = models.DecimalField(max_digits=5,decimal_places=2, default=0.8) #港币汇率
	index_sh = models.DecimalField(max_digits=8,decimal_places=2,default=0) #上证
	index_sz = models.DecimalField(max_digits=8,decimal_places=2,default=0)  #深证
	index_zxb = models.DecimalField(max_digits=8,decimal_places=2,default=0) #中小板
	index_cyb = models.DecimalField(max_digits=8,decimal_places=2,default=0) #创业板
	index_sh_pct = models.DecimalField(max_digits=8,decimal_places=4,default=0) #上证变动比率
	index_sz_pct = models.DecimalField(max_digits=8,decimal_places=4,default=0) #深证变动比率
	index_zxb_pct = models.DecimalField(max_digits=8,decimal_places=4,default=0) #中小板变动比率
	index_cyb_pct = models.DecimalField(max_digits=8,decimal_places=4,default=0) #创业板变动比率
	net_value = models.DecimalField(max_digits=20,decimal_places=2,default=0)
	net_change = models.DecimalField(max_digits=20,decimal_places=2,default=0) #绝对净值变动
	net_pct = models.DecimalField(max_digits=8,decimal_places=4,default=0) #净值变动百分比
	abs_pct = models.DecimalField(max_digits=8,decimal_places=4,default=0) #与期初比较百分比
	def __unicode__(self):              # __unicode__ on Python 2
		return str(self.trade_date) + '(' + str(self.invest_plan) + ')'
	def save(self, *args, **kwargs):
		plan = self.invest_plan
		new_net_value = self.rmb_total_value + (self.hkd_total_value * self.hkd_rmb) #新净值
		old_net_value = plan.net_value
		self.net_value = new_net_value
		plan.net_value = new_net_value
		self.abs_pct = self.net_value / plan.begin_value
		last_id = TradeLog.objects.filter(invest_plan=plan).aggregate(Max('id'))
		print last_id['id__max']
		if last_id['id__max']:
			#we have a previous row
			last_record = TradeLog.objects.get(id=last_id['id__max'])
			self.net_change = self.net_value - last_record.net_value
			self.net_pct = self.net_value / last_record.net_value
		super(TradeLog, self).save(*args, **kwargs) # Call the "real" save() method.
		plan.save()
		

	
	
	
