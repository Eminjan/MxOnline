#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:Eminjan
#@Time  :2018/4/17 14:44

import xadmin
from .models import Course,Lesson,Video,CourseResource,BannerCourse


class LessonInline(object):
    model = Lesson
    extra = 0

class CourseResourseInline(object):
    model = CourseResource
    extra = 0

class CourseAdmin(object):
    list_display = ['name','degree','learn_times','students','click_nums','add_time','get_zj_nums']
    search_fields = ['name','degree','learn_times','students','click_nums']
    list_filter = ['name','degree','learn_times','students','click_nums','add_time']
    model_icon = 'fa fa-database'
    ordering = ['-click_nums']
    list_editable = ['degree','click_nums']
    readonly_fields = ['fav_nums','students','learn_times']

    inlines = [LessonInline,CourseResourseInline]



class BannerCourseAdmin(object):
    list_display = ['name','degree','learn_times','students','click_nums','add_time']
    search_fields = ['name','degree','learn_times','students','click_nums']
    list_filter = ['name','degree','learn_times','students','click_nums','add_time']
    model_icon = 'fa fa-database'
    ordering = ['-click_nums']
    readonly_fields = ['fav_nums','students','learn_times']
    exclude = ['click_nums']
    inlines = [LessonInline,CourseResourseInline]

    def queryset(self):
        qs=super(BannerCourseAdmin,self).queryset()
        qs.filter(is_banner = True)
        return qs

class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course','name','add_time']
    model_icon = 'fa fa-bars'

class VideoAdmin(object):
    list_display = ['lesson', 'name','add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name','add_time']
    model_icon = 'fa fa-film'

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']
    model_icon = 'fa fa-folder-open'

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)