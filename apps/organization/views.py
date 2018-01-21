# -*- coding:utf-8 -*-
import json
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q
from .forms import UserAskForm
from django.http import HttpResponse
from .models import CourseOrg, CityDict, Teacher
from courses.models import Course
from operation.models import UserFavorite


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()

        # 提取热门机构
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        # 城市
        all_citys = CityDict.objects.all()

        # 机构搜索
        serach_keywords = request.GET.get('keywords', "")
        if serach_keywords:
            all_orgs = all_orgs.filter(
                Q(name__icontains=serach_keywords) | Q(desc__icontains=serach_keywords))

        # 取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            # 筛选出当前城市的结果集
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            # 筛选出当前城市的结果集
            all_orgs = all_orgs.filter(category=category)

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-courses_nums")
        org_nums = all_orgs.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 2, request=request)

        orgs = p.page(page)

        current_nav = 'org'
        return render(request, 'org-list.html', {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_orgs": hot_orgs,
            "sort": sort,
            'current_nav': current_nav,
        })


class AddUserAskView(View):
    def post(self,request):
        userask_form =UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}',content_type='application/json')
class OrgHomeView(View):
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request,"org-detail-homepage.html",{'all_courses':all_courses,'all_teachers':all_teachers,'course_org':course_org})


