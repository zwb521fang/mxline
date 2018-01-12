#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/12 15:02'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)