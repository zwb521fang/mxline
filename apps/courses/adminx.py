#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/11 14:42'
import xadmin
from .models import Course,Lesson,CourseOrg,CourseResource,Video

class CourseAdmin(object):
    list_display = ['course_org', 'name', 'desc', 'detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields = ['course_org', 'name', 'desc', 'detail','degree','learn_times','students','fav_nums','image','click_nums']
    list_filter = ['course_org', 'name', 'desc', 'detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']


class LessonAdmin(object):
    list_display = ['course', 'name',  'add_time']
    search_fields =  ['course', 'name', ]
    list_filter = ['course', 'name',  'add_time']
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Course, CourseAdmin)
