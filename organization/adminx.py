#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:Eminjan
#@Time  :2018/4/17 16:40

import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    model_icon = 'fa fa-car'

class CourseOrgAdmin(object):
    list_display = ['name', 'desc','click_nums','fav_nums','address','city','add_time']
    search_fields = ['name','click_nums','fav_nums','address','city']
    list_filter = ['name','click_nums','fav_nums','city','add_time']
    model_icon = 'fa fa-university'
    refield_style = 'fk-ajax'

class TeacherAdmin(object):
    list_display = ['name', 'age','org', 'work_years', 'work_company', 'work_position', 'click_nums','fav_nums', 'add_time']
    search_fields = ['name', 'age','org', 'work_years', 'work_company', 'work_position', 'click_nums','fav_nums']
    list_filter = ['name', 'age','org', 'work_years', 'work_company', 'work_position','click_nums','fav_nums', 'add_time']
    model_icon = 'fa fa-user-o'

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)

