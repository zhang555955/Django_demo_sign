#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: 橘子
# @Date  : 2020/9/21
# @Desc  : execise
from __future__ import unicode_literals
from django.contrib import admin
from .models import Student

# Register your models here.

admin.site.register(Student)