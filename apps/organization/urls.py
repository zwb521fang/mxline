#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/21 17:58'
from django.conf.urls import url,include
from organization.views import OrgView,AddUserAskView,OrgHomeView
urlpatterns = [
    #课程机构首页
    url('^list/$', OrgView.as_view(), name='org_list'),
    url('^add_ask',AddUserAskView.as_view(),name='add_ask'),
    url('^home/(?P<org_id>\d+)/$',OrgHomeView.as_view(),name="org_home"),
]