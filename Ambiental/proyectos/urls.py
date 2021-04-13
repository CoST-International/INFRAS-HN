# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('proyectos.views',
    #url(r"^posicion_puntos$", "tabla_puntos", name="tabla_puntos"),
    url(r"^todos$", "proyectos_todos", name="proyectos_todos"),
    url(r"^(?P<mod_id>\d+)/detalle$", "proyectos_detalle", name="proyectos_detalle"),
    #url(r"^(?P<mod_id>\d+)/detalle$", "detalle_proyecto", name="detalle_proyecto"),
    #url(r"^proyectos/todos$", "detalle_proyecto", name="detalle_proyecto"),
    #url(r"^puntos/fecha$", "puntos_actuales_fecha", name="puntos_actuales_fecha"),
    #url(r"^puntos_usuarios$", "puntos_usuarios", name="puntos_usuarios"),
    #url(r"^obtener_proyecto$", "obtener_proyecto", name="obtener_proyecto"),
	#url(r"^puntos_usuarios/hoy$", "puntos_usuarios_hoy", name="puntos_usuarios_hoy"),
	#url(r"^puntos_usuariosfecha$", "puntos_usuarios_fecha", name="puntos_usuarios_fecha"),
    #url(r"^puntos_usuarios/manana$", "puntos_usuarios_manana", name="puntos_usuarios_manana"),
    
    #url(r"^(?P<mod_id>\d+)/detalle$", "detalle_cliente", name="detalle_cliente"),
    #url(r"^busca_cliente$", "busca_cliente", name="busca_cliente"),

)