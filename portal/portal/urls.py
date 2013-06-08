#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index', name='index'),
    # url(r'^portal/', include('portal.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
