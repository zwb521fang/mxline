#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/12 15:02'

from django import forms
from  captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,max_length=6)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})
class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, max_length=6)
    password2 = forms.CharField(required=True, max_length=6)