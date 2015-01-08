# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone

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

class Investors(models.Model):
	full_name = models.CharField(max_length=50)  #姓名
	share_rights = models.IntegerField() #权益分额
	principal = models.DecimalField(max_digits=20,decimal_places=2)  #本金金额
	invest_plan = models.ForeignKey(InvestPlan)	
	
class TradeLog(models.Model):
	trade_date = models.DateField()
	a_stock_value = models.DecimalField(max_digits=20,decimal_places=2)
	h_stock_value = models.DecimalField(max_digits=20,decimal_places=2)
	rmb_cash_value = models.DecimalField(max_digits=20,decimal_places=2)
	hkd_cash_value = models.DecimalField(max_digits=20,decimal_places=2)
	hkd_rmb = models.DecimalField(max_digits=5,decimal_places=2) #港币汇率
	index_sh = models.DecimalField(max_digits=8,decimal_places=2) #上证
	index_sz = models.DecimalField(max_digits=8,decimal_places=2)  #深证
	index_zxb = models.DecimalField(max_digits=8,decimal_places=2) #中小板
	index_cyb = models.DecimalField(max_digits=8,decimal_places=2) #创业板
	index_sh_pct = models.DecimalField(max_digits=8,decimal_places=4) #上证变动比率
	index_sz_pct = models.DecimalField(max_digits=8,decimal_places=4) #深证变动比率
	index_zxb_pct = models.DecimalField(max_digits=8,decimal_places=4) #中小板变动比率
	index_cyb_pct = models.DecimalField(max_digits=8,decimal_places=4) #创业板变动比率
	
	
	