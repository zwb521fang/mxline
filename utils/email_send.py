#coding=utf-8
__author__ = 'zwb'
__date__ = '2018/1/13 13:41'
from random import Random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from  mx.settings import  EMAIL_FROM

def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    code = generate_random_str(16)
    email_record.code=code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()


    if send_type =="register":
        email_title = "暮雪在线网注册激活链接"
        email_body = "请点击下边的链接，激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type=='forget':
        email_title = "暮雪在线网注册重置链接"
        email_body = "请点击下边的链接，重置你的账号：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
def generate_random_str(randomlength=8):
    str =''
    chars = "AaBaCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqSsTtUuVvWwZz0123456789"
    length = len(chars)-1
    random =Random()
    for i in range(randomlength):
        str+= chars[random.randint(0,length)]
    return str



