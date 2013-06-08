#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nscms.simplenews.models import SimpleNews


def portal(context):
    return  {
        'simplenews_latest': SimpleNews.objects.published()[:5]
    }
