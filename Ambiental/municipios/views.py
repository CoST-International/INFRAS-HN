# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from proyectos.models import Proyectos
from datetime import datetime, date, time, timedelta

def proyectos_todos(request):
    ddic = {}
    ddic['proyectos'] = Proyectos.objects.all()
    return render_to_response('proyectos_todos.html',ddic,context_instance=RequestContext(request))

def proyectos_detalle(request,mod_id=None):
    ddic = {}
    ddic['proyecto'] = Proyectos.objects.get(pk=mod_id)
    return render_to_response('proyectos_detalle.html',ddic,context_instance=RequestContext(request))

"""def tabla_puntos(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['puntos'] = Puntos.objects.all().order_by('-puntos','nombre')
    today = datetime.today()
    print(today)
    return render_to_response('tabla_puntos.html',ddic,context_instance=RequestContext(request))

def puntos_actuales(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['partidos'] = Enfrentamiento.objects.all().order_by('fecha_enfrentamiento')
    ddic['puntos'] = Puntos.objects.filter(usuario=request.user)
    ddic['pronostico'] = Pronostico.objects.filter(usuario=request.user).order_by('id_enfrentamiento__fecha_enfrentamiento')

    return render_to_response('puntos_actuales.html',ddic,context_instance=RequestContext(request))

def puntos_actuales_hoy(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    today = datetime.today()
    ddic['partidos'] = Enfrentamiento.objects.filter(fecha_enfrentamiento__contains=today.strftime('%Y-%m-%d')).order_by('fecha_enfrentamiento')
    ddic['puntos'] = Puntos.objects.filter(usuario=request.user)
    ddic['pronostico'] = Pronostico.objects.filter(usuario=request.user,id_enfrentamiento=ddic['partidos'])
    return render_to_response('puntos_actuales.html',ddic,context_instance=RequestContext(request))

def puntos_actuales_fecha(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['fecha'] = request.GET['fecha']
    ddic['partidos'] = Enfrentamiento.objects.filter(fecha_enfrentamiento__contains=ddic['fecha']).order_by('fecha_enfrentamiento')
    ddic['puntos'] = Puntos.objects.filter(usuario=request.user)
    ddic['pronostico'] = Pronostico.objects.filter(usuario=request.user,id_enfrentamiento=ddic['partidos']).order_by('id_enfrentamiento')
    return render_to_response('puntos_actuales.html',ddic,context_instance=RequestContext(request))

def puntos_usuarios(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
        today = datetime.today()
    dias = timedelta(days=1)
    today = datetime.today()-dias
    ddic['partidos'] = Enfrentamiento.objects.filter(fecha_enfrentamiento__lt=today).order_by('fecha_enfrentamiento')
    ddic['usuarios']= Puntos.objects.all().order_by('nombre') 
    ddic['pronostico'] = Pronostico.objects.all().order_by('id_enfrentamiento').order_by('id_enfrentamiento__fecha_enfrentamiento')
    return render_to_response('usuarios_puntos_todos.html',ddic,context_instance=RequestContext(request))

def puntos_usuarios_manana(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    today = datetime.today()
    dias = timedelta(days=1)
    today = datetime.today()+dias
    ddic['partidos'] = Enfrentamiento.objects.filter(fecha_enfrentamiento__contains=today.strftime('%Y-%m-%d')).order_by('fecha_enfrentamiento')
    ddic['pronostico'] = Pronostico.objects.filter(id_enfrentamiento=ddic['partidos']).order_by('id_enfrentamiento__fecha_enfrentamiento')
    ddic['pronostico_1']=Pronostico.objects.filter(id_enfrentamiento=ddic['partidos'],usuario=request.user).order_by('id_enfrentamiento__fecha_enfrentamiento')
    ddic['usuarios']= Puntos.objects.all().order_by('nombre')
    return render_to_response('usuarios_puntos_manana.html',ddic,context_instance=RequestContext(request))

def puntos_usuarios_hoy(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    today = datetime.today()
    ddic['partidos'] = Enfrentamiento.objects.filter(fecha_enfrentamiento__contains=today.strftime('%Y-%m-%d')).order_by('fecha_enfrentamiento')
    ddic['pronostico'] = Pronostico.objects.filter(id_enfrentamiento=ddic['partidos']).order_by('id_enfrentamiento__fecha_enfrentamiento')
    ddic['pronostico_1']=Pronostico.objects.filter(id_enfrentamiento=ddic['partidos'],usuario=request.user).order_by('id_enfrentamiento__fecha_enfrentamiento')
    ddic['usuarios']= Puntos.objects.all().order_by('nombre')
    return render_to_response('usuarios_puntos.html',ddic,context_instance=RequestContext(request))

def puntos_usuarios_fecha(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['fecha'] = request.GET['fecha']
    ddic['partidos'] = Enfrentamiento.objects.filter(fecha_enfrentamiento__contains=ddic['fecha']).order_by('fecha_enfrentamiento')
    ddic['pronostico_1']=Pronostico.objects.filter(id_enfrentamiento=ddic['partidos'],usuario=request.user).order_by('id_enfrentamiento__fecha_enfrentamiento')
    ddic['pronostico'] = Pronostico.objects.filter(id_enfrentamiento=ddic['partidos']).order_by('id_enfrentamiento__fecha_enfrentamiento')
    ddic['usuarios']= Puntos.objects.all().order_by('nombre')
    return render_to_response('usuarios_puntos.html',ddic,context_instance=RequestContext(request))


def puntos_usuario(request):
    ddic = {}
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    ddic['usuario'] = request.GET['usuario']
    ddic['partidos'] = Enfrentamiento.objects.all().order_by('fecha_enfrentamiento')
    ddic['usuarios']= Puntos.objects.all().order_by('nombre')
    ddic['pronostico_1']=Pronostico.objects.filter(id_enfrentamiento=ddic['partidos'],usuario=request.user).order_by('id_enfrentamiento__fecha_enfrentamiento')
    ddic['pronostico'] = Pronostico.objects.filter(usuario=ddic['usuario']).order_by('id_enfrentamiento__fecha_enfrentamiento')
    return render_to_response('usuarios_puntos.html',ddic,context_instance=RequestContext(request))

"""