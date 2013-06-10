#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib.admin import site

from .models import Slot, Portlet


site.register(Slot)


site.register(Portlet)
