#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: 橘子
# @Date  : 2020/9/21
# @Desc  : execise
from sys import path

from django.conf.urls import url

from . import views

urlpatterns = {
    url('^$', views.index_view),
    url('^show/$', views.show_view),
    url('^login/$', views.login_view)
}