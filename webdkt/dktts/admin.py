# -*- coding: utf-8 -*-
from django.contrib import admin
from polls.models import Question,InvestPlan,Investor,TradeLog
# Register your models here.
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('full_name','share_rights', 'principal','net_value')

admin.site.register(Question)
admin.site.register(InvestPlan)
admin.site.register(Investor,InvestorAdmin)
admin.site.register(TradeLog)
