#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/11 18:11'
from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse
import xadmin


class UserAskAdmin(object):
    list_display = [ 'name', 'mobile','add_time','course_name']
    search_fields = [ 'name', 'mobile','course_name']
    list_filter = [ 'name', 'mobile','add_time','course_name']


class CourseCommentsAdmin(object):
    list_display = [ 'user', 'course','comments','add_time']
    search_fields =  [ 'user', 'course','comments']
    list_filter =[ 'user', 'course','comments','add_time']



class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id',  'add_time','fav_type']
    search_fields =  ['user', 'fav_id','fav_type']
    list_filter = ['user', 'fav_id',  'add_time','fav_type']
class UserMessageAdmin(object):
    list_display = ['user', 'message',  'add_time','has_read']
    search_fields =  ['user', 'message','has_read']
    list_filter = ['user', 'message',  'add_time','has_read']
class UserCourseAdmin(object):
    list_display = ['user', 'course',  'add_time']
    search_fields = ['user', 'course']
    list_filter =['user', 'course',  'add_time']


xadmin.site.register(UserMessage,UserAskAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserFavorite,UserCourseAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
