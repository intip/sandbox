#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db.models import Model
from django import template

from classytags.core import Options
from classytags.helpers import InclusionTag
from classytags.arguments import MultiValueArgument

from slot import models


register = template.Library()


class Slot(InclusionTag):
    name = 'slot'
    template = 'slot/slot.html'
    options = Options(
#        MultiValueArgument("tagname"),
#        KeywordArgument("tagname", required=True, resolve=True),
        MultiValueArgument('keys', required=True, resolve=True),
#        blocks=[('endplaceholder_objects', 'nodelist', )],
    )

    def get_context(self, context, keys):
        parts = []
        for part in [k for k in keys if k]:
            if isinstance(part, Model):
                key = u"%s,%s,%d" % (
                    part._meta.app_label, part.__class__.__name__, part.pk)
            else:
                key = unicode(part)
            parts.append(key)

        key = u"|".join([unicode(i) for i in parts])
        slot, created = models.Slot.objects.get_or_create(key=key)
        return {"slot": slot}


register.tag(Slot)
