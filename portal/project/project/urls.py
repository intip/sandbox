#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True
    }),
    url(r'^slot/', include("slot.urls", namespace="slot")),
    url(r'^$', 'frontend.views.index', name='index'),
    url(r'^ckeditor/', include("ckeditor.urls")),
    url(r'^placeholder/', include("placeholder.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
