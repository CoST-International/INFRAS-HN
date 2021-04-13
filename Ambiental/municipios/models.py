# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField

class Municipios(models.Model):
    departamento=models.CharField(max_length='125', verbose_name=u'Nombre Departamento:')
    municipio=models.CharField(max_length='125', verbose_name=u'Nombre Municipio:')
    superficie=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Superficie Km2:')
    poblacion=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Población (2013):')
    hombres=models.IntegerField(null=True,blank=True, verbose_name=u'Poblacion Hombres:')
    mujeres=models.IntegerField(null=True,blank=True, verbose_name=u'Poblacion Mujeres:')
    poblacion_estimada=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Poblacion Estimada (2015):')
    aldeas=models.IntegerField(null=True,blank=True, verbose_name=u'Numero de Aldeas:')
    asentamientos=models.IntegerField(null=True,blank=True, verbose_name=u'Numero de Asentamientos:')
    densidad=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Densidad (Hab/km2):')
    poblacion_economicamenteactiva=models.IntegerField(null=True,blank=True, verbose_name=u'Población Economicamente Activa (2013):')
    indice_ingreso=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Indice Ingreso (2009):')
    ingreso_epa=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Indice Estimado Percapita Anual ($):')
    superficie_microcuencas=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Superficie Km2 Microcuencas (2013):')
    numero_microcuencas=models.IntegerField(null=True,blank=True, verbose_name=u'Numero de Microcuencas declaradas:')
    superficie_areasprotegidas=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Superficie en Areas Protegidas (2013)')
    superficie_bosques=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Superficie Cubiera de bosques (ha)')
    superficie_sinbosque=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Superficie tierra sin bosques (ha)')
    densidad_redvial=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Densidad red vial (Km/Km2):')
    red_vialpavimentada=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Red Vial Pavimentada (Km):')
    red_vialsecundaria=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Red Vial Secundaria (km):')
    carretera_materialprimario=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Carretera Material Selecto Primario:')
    carretera_materialsecundario=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Carretera Material Selecto Secundario:')
    carretera_materialvecinal=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Carretera Material Selecto Vecinal:')
    carretera_tierraprincipal=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Carretera Tierra Principal:')
    carretera_materialtierravecinal=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Carretera Material Tierra Vecinal:')
    totalidad_vialidadmunicipal=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name=u'Total de Vialidad Municipal (Km):')
    def __unicode__(self):
                return '%s %s' % (self.departamento,self.municipio)


