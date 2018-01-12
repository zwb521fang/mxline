#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from .models import UserProfile
from .forms import LoginForm,RegisterForm
from  django.contrib.auth.hashers import make_password

class CustomBackend(ModelBackend):
      def authenticate(self, username=None, password=None, **kwargs):
          try:
              user = UserProfile.objects.get(Q(username=username)| Q(email=username))
              if user.check_password(password):
                  return user
          except Exception as e:
              return None
class LoginView(View):
#基于类的第二种写法
    def get(self,request):
        return render(request, "login.html")
    def post(self,request):
        if request.method == "POST":
            login_form = LoginForm(request.POST)#判断字段是否必填
            if login_form.is_valid():
                user_name = request.POST.get('username', '')
                pass_word = request.POST.get('password', '')
                user = authenticate(username=user_name, password=pass_word)
                if user is not None:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户名或密码错误"})
            else:
                return render(request, "login.html", {"login_form":login_form})

# def user_login(request)://第一种写法
#     if request.method == "POST":
#         user_name = request.POST.get('username','')
#         pass_word = request.POST.get('password','')
#         user = authenticate(username = user_name,password=pass_word)
#         if user is not None:
#             login(request,user)
#             return  render(request,"index.html")
#         else:
#             return render(request, "login.html",{"msg":"用户名或密码错误"})
#     elif request.method == "GET":
#         return render(request,"login.html")’

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/login/")
class RegisterView(View):
    def get(self,request):
        register_form =RegisterForm()#生成验证码
        return render(request, "register.html",{'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username =user_name
            user_profile.email    =user_name
            user_profile.password  =make_password(pass_word)
            user_profile.save()

