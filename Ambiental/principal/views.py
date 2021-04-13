# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from proyectos.models import Proyectos
from municipios.models import Municipios
from django.template import RequestContext
from datetime import datetime, date, time, timedelta

def main(request):
    ddic = {}
    if request.method == "POST":
    	ddic['nombre']=request.POST['nombre']
        if request.POST.get('c1', False):
            ddic['proyectos']=Proyectos.objects.filter(valida_ambiental=1)
        elif request.POST.get('c2', False):
            ddic['proyectos']=Proyectos.objects.filter(valida_ambiental=2)
        elif request.POST.get('c3', False):
            ddic['proyectos']=Proyectos.objects.filter(valida_ambiental=3)
        elif request.POST.get('c4', False):
            ddic['proyectos']=Proyectos.objects.filter(valida_ambiental=4)
        elif request.POST.get('cons', False):
            ddic['proyectos']=Proyectos.objects.filter(tipo_obra__contains='construcci')
        elif request.POST.get('reha', False):
            ddic['proyectos']=Proyectos.objects.filter(tipo_obra__contains='rehabilitaci')
        elif request.POST.get('mant', False):
            ddic['proyectos']=Proyectos.objects.filter(tipo_obra__contains='mantenimiento')
        else:
            ddic['proyectos']=Proyectos.objects.filter(nombre__contains=ddic['nombre'])
        ddic['latitud']=15.00
        ddic['longitud']= -86.5000000
    else:
    	ddic['proyectos']=Proyectos.objects.all()
        ddic['latitud']=14.60
        ddic['longitud']=-86.5000000
    return render_to_response('main.html',ddic,context_instance=RequestContext(request))

def busca(request):
    ddic = {}
    ddic['proyectos']=Proyectos.objects.all()
    return render_to_response('main.html',ddic,context_instance=RequestContext(request))

def como_utilizar(request):
    ddic = {}
    return render_to_response('como_utilizar.html',ddic,context_instance=RequestContext(request))

def licencias(request):
    ddic = {}
    return render_to_response('licencias.html',ddic,context_instance=RequestContext(request))

def reporte(request):
    ddic = {}
    ddic['c1']=Proyectos.objects.filter(valida_ambiental=1).count()
    ddic['c2']=Proyectos.objects.filter(valida_ambiental=2).count()
    ddic['c3']=Proyectos.objects.filter(valida_ambiental=3).count()
    ddic['c4']=Proyectos.objects.filter(valida_ambiental=4).count()
    return render_to_response('info_proyectos.html',ddic,context_instance=RequestContext(request))

def contacto(request):
    ddic = {}
    return render_to_response('contacto.html',ddic,context_instance=RequestContext(request))
