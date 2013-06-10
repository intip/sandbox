#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin

from .models import Basico, Noticia, UltimasNoticias, HTML


class PortletAdmin(admin.ModelAdmin):
    save_on_top = True


admin.site.register(Basico, PortletAdmin)
admin.site.register(Noticia, PortletAdmin)
admin.site.register(UltimasNoticias, PortletAdmin)
admin.site.register(HTML, PortletAdmin)
