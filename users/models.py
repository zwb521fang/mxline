#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from  datetime import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default='')
    birday  = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length =5,choices=(("male",u"男"),("female",u'女')),default='female')
    address = models.CharField(max_length=100,default=u'地址')
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%y/%m",default=u"image/default.png",max_length=100)
    class Meta:
        verbose_name ='用户信息'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return  self.username
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(("register",u"注册",("forget",u"找回密码")),max_length=50)
    send_time = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name=u'邮箱验证'
        verbose_name_plural = verbose_name
class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图",max_length=100)
    utl = models.URLField(max_length=200,verbose_name=u"访问地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    class Meta:
        verbose_name=u"轮播图"
        verbose_name_plural = verbose_name
