#coding=utf-8
"""mx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.contrib import admin
from django.views.generic import TemplateView
from users.views import LoginView,logout_view,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView
import xadmin
from mx.settings import MEDIA_ROOT
from  django.views.static import serve
urlpatterns = [
    url('^captcha', include('captcha.urls')),
    url(r'^xadmin/', xadmin.site.urls),
    url('^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^logout/$', logout_view, name='logout'),
    url('^register/$',RegisterView.as_view(),name='register'),
    url('^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url('^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url('^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url('^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
    url('^org_list/$', OrgView.as_view(), name='org_list'),
    #配置上传文件的访问
    url('^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),




]
