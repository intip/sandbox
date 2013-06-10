#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render

from .models import Portlet


def portlet_choose(request):
    return render(request, "slot/portlet_choose.html", {
        'portlet_classes': Portlet.classes,
    })
