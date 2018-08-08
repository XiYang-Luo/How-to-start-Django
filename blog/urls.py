# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 18:05:48 2018

@author: luo xi yang
"""

from django.conf.urls import url
from . import views
#from blog.views import index
app_name='blog' '''https://www.cnblogs.com/demonszz/p/8329846.html解决了这个问题'''
urlpatterns = [
    url(r'^index',views.index),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name="edit_page"),
    url(r'^edit/action$',views.edit_action,name='edit_action'),
]
