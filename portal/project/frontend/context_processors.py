#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nscms.simplenews.models import SimpleNews


def portal(context):
    qs = SimpleNews.objects.published()
    if qs.exists():
        featured = qs[0]
    else:
        featured = None
    return  {
        'simplenews_featured': featured,
        'simplenews_latest': qs[1:6],
    }
