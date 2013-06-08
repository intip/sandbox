#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models


class Portlet(models.Model):
    pass


class Slot(models.Model):
    key = models.TextField(db_index=True, unique=True)
    portlets = models.ManyToManyField("Portlet")
