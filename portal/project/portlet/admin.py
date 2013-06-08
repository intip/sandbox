#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin

from .models import Basico


class BasicoAdmin(admin.ModelAdmin):
    save_on_top = True


admin.site.register(Basico, BasicoAdmin)
