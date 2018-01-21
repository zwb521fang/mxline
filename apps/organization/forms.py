#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/17 21:02'
from django import forms

class UserAskForm(forms.Form):
    name = forms.CharField(required=True,mix_length=2,max_length=20)
    phone = forms.CharField(required=True,min_length=11,max_length=11)
    course_name = forms.CharField(required=True,min_length=2,max_length=50)