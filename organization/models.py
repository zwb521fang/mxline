#coding = utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from  datetime import datetime

class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    desc = models.CharField(max_length=300, verbose_name=u"机构描述")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名")
    desc = models.CharField(max_length=300, verbose_name=u"机构描述")
    # detail = models.TextField(verbose_name=u"课程详情")
    # degree = models.CharField(choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=300)
    # learn_times = models.IntegerField(default=0, verbose_name=u"学习时长")
    # students = models.IntegerField(default=0, verbose_name=u"学习人数", max_length=10)
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数", max_length=10)
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(max_length=20, default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    address = models.CharField(max_length=100, default=u'地址')
    city = models.ForeignKey(CityDict,verbose_name=u"所在城市")
    # location = models.CharField(max_length=50,verbose_name=u"通讯详细地址")
    # has_auth = models.BooleanField(verbose_name=u"是否验证",default=False)


    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u"所属机构")
    name = models.CharField(max_length=50,verbose_name=u"教师名")
    work_years = models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(default=0,verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50,verbose_name=u"公司职位")
    points  = models.CharField(max_length=50,verbose_name=u"教学特点")
    click_nums = models.IntegerField(max_length=20, default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数", max_length=10)

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

