#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models

from slot.models import Portlet


class HTML(Portlet):
    titulo = models.CharField(max_length=100)
    code = models.TextField()


class UltimasNoticias(Portlet):
    numero = models.PositiveIntegerField(default=5)


class Noticia(Portlet):
    simplenews = models.ForeignKey("simplenews.SimpleNews", unique=True)


class Basico(models.Model):
    titulo = models.CharField(u"Título", max_length=100)
    imagem = models.ImageField(upload_to="portlet/%Y/%m/%d")
    imagem_posicao = models.CharField(u"Posição da Imagem", choices=(
        ('', 'Nenhuma'),
        ('left', 'Esquerda'),
        ('right', 'Direita'),
    ), max_length=5, blank=True)
    texto = models.TextField()

    class Meta:
        ordering = ("id", )
        verbose_name = u"Portlet Básico"
        verbose_name_plural = u"Portlets Básicos"

    def __unicode__(self):
        return self.titulo 
