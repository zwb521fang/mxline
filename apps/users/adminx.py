#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/10 20:07'

from .models import EmailVerifyRecord
from .models import *
from xadmin import views
import xadmin

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter =['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'add_time']
    search_fields = ['title', 'image', 'url']
    list_filter = ['title', 'image', 'url', 'add_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
