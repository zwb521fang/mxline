# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from organization.models import CourseOrg, Teacher

# Create your models here.
class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name="课程机构", null=True, blank=True)
    name = models.CharField(max_length=50,verbose_name=u"课程名")
    desc = models.CharField(max_length=300,verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name='难度',choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=300)
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长")
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面图",max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    add_time   = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return  self.name
    def __str__(self):
            return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name

class Video(models.Model):
    Lesson = models.ForeignKey(Lesson,verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name

class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u"路径",max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资料"
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name



