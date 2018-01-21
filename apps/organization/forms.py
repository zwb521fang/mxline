#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/17 21:02'
from django import forms
from  operation.models import UserAsk
import re
# class UserAskForm(forms.Form):#第一种写法
#     name = forms.CharField(required=True,mix_length=2,max_length=20)
#     phone = forms.CharField(required=True,min_length=11,max_length=11)
#     course_name = forms.CharField(required=True,min_length=2,max_length=50)


#继承userAsk   model
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']
    def clean_mobile(self):
        mobile = self.changed_data['mobile']
        REGEX_MOBILE = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$"
        p =re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            return  forms.ValidationError(u"手机号码非法",code=mobile)
