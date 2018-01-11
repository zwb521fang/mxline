#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/11 18:11'
from .models import CityDict,CourseOrg,Teacher
import xadmin


class CityDictAdmin(object):
    list_display = [ 'name', 'desc','add_time']
    search_fields = [ 'name', 'desc']
    list_filter = [ 'name', 'desc','add_time']

class CourseOrgAdmin(object):
    list_display = ['desc', 'name',  'add_time','fav_nums','image','click_nums','address','city']
    search_fields =  ['desc', 'name','fav_nums','image','click_nums','address','city']
    list_filter = ['desc', 'name',  'add_time','fav_nums','image','click_nums','address','city']


class TeacherAdmin(object):
    list_display = ['org', 'name',  'add_time','work_years','work_company','click_nums','work_position','points','fav_nums']
    search_fields = ['org', 'name', 'work_years','work_company','click_nums','work_position','points','fav_nums']
    list_filter =['org', 'name',  'add_time','work_years','work_company','click_nums','work_position','points','fav_nums']




xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
