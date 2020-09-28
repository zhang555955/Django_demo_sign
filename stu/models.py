#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: 橘子
# @Date  : 2020/9/21
# @Desc  : execise

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField(max_length=30,unique=True)
    spwd = models.CharField(max_length=30)

    def __str__(self):
        return u'Student:%s'%self.sname

    # class Mota:
    #     managed = False
    #     db_table = 't_stu'

