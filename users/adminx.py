#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:Eminjan
#@Time  :2018/4/17 13:55

import xadmin
from xadmin import views

from .models import UserProfile,EmailVerifyRecord,Banner
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = 'Mx Online 后台管理'
    site_footer = 'Mx Online'
    # menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']
    model_icon = 'fa fa-address-book-o'
class BannerAdmin(object):
    list_display = ['title','url','index','add_time']
    search_fields = ['title','index']
    list_filter = ['title','url','index','add_time']
    model_icon = 'fa fa-file-image-o'

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)

