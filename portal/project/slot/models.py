#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.db.models import signals
from django.db import models


class Portlet(models.Model):
    classes = []
    classname = models.CharField(max_length=100, db_index=True, editable=False)


def class_prepared(sender, *args, **kwargs):
    if issubclass(sender, Portlet):
        Portlet.classes.append({
            'name': sender.__name__,
            'url': reverse_lazy(
                "admin:%s_%s_add" % (
                    sender._meta.app_label,
                    sender.__name__.lower())
            ),
        })


signals.class_prepared.connect(class_prepared)


def pre_save(sender, instance, raw, using, *args, **kwargs):
    if issubclass(sender, Portlet):
        instance.classname = sender.__name__


signals.pre_save.connect(pre_save)


class Slot(models.Model):
    key = models.TextField(db_index=True, unique=True)
    portlets = models.ManyToManyField("Portlet")
