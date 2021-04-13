# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField

class Proyectos(models.Model):
    numero=models.IntegerField(null=True,blank=True, verbose_name=u'Numero:')
    nombre=models.CharField(max_length='125', verbose_name=u'Nombre Proyecto:')
    descripcion=models.CharField(max_length='125', verbose_name=u'Descripcion Proyecto:')
    latitud=models.DecimalField(null=True,max_digits=10,decimal_places=5,verbose_name=u'Latitud')
    longitud=models.DecimalField(null=True,max_digits=10,decimal_places=5,verbose_name=u'Longitud')
    fecha_inicio=models.DateTimeField(auto_now=False,blank=True,null=True)
    fecha_fin=models.DateTimeField(auto_now=False,blank=True,null=True)
    tipo_obra=models.CharField(max_length='25',blank=True, verbose_name=u'Tipo Proyecto:')
    precio=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Precio:')
    ente_responsable=models.CharField(max_length='25',blank=True, verbose_name=u'Ente Proyecto:')
    departamento=models.CharField(max_length='25', verbose_name=u'Departamento Proyecto:')
    municipio=models.CharField(max_length='25', verbose_name=u'Municipio Proyecto:')
    licencia_ambiental_sisocs=models.CharField(max_length='25', verbose_name=u'Licencia Ambiental SISOCS:')
    categoria_ambiental=models.IntegerField(null=True,blank=True, verbose_name=u'Numero:')
    valida_ambiental=models.IntegerField(null=True,blank=True, verbose_name=u'Validacion Ambiental:')
    url_sisocs=models.CharField(max_length='125',blank=True, verbose_name=u'URL Proyecto:')
    imagen=models.ImageField(upload_to="imagen_proyecto/",blank=True)
    pib=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'PIB:')
    def __unicode__(self):
        return '[ %s ] - %s - %s ' % (self.numero, self.precio, self.fecha_inicio)


