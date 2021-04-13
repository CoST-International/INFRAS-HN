# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('principal.views',

    url(r"^$", "main", name="main"),
    url(r"como_utilizar/$", "como_utilizar", name="como_utilizar"),
    url(r"licencias/$", "licencias", name="licencias"),
    url(r"contacto/$", "contacto", name="contacto"),
    url(r"^busca/$", "busca", name="busca"),
    url(r"^reporte/$", "reporte", name="reporte"),


)