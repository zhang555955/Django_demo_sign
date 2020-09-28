#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: 橘子
# @Date  : 2020/9/21
# @Desc  : execise

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index_view(request):
    # 获取当前请求方式（GET/POST）
    m = request.method
    if m == 'GET':
        return render(request, 'register.html')
    else:
        # 获取请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        # 判断
        if uname and pwd:
            # 创建数据库模型对象
            stu = Student(sname=uname, spwd=pwd)
            # 插入保存到数据库
            stu.save()
            return HttpResponse('注册成功')
        return HttpResponse('注册失败')


def show_view(request):
    # 1.查询stu_student表中所有数据
    stus = Student.objects.all()
    return render(request, 'show.html', {'students': stus})


def login_view(request):
    #判断当前请求方式
    if request.method=='GET':
        return render(request, 'login.html')
    else:
        #1.获取请求参数
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        #2.查询数据库
        if uname and pwd:
            c = Student.objects.filter(sname=uname,spwd=pwd).count()
            if c == 1:
                return HttpResponse('登录成功！')
        #3.判断是否登录成功
        return HttpResponse('登录失败！'）