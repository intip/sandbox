#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('slot.views',
    url(r'^portlet/choose/$', 'portlet_choose', name='portlet_choose'),
)
