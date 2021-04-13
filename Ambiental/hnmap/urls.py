from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('principal.urls')),
    url(r'^proyectos/', include('proyectos.urls')),
    url(r'^municipios/', include('municipios.urls')),


)
if settings.DEBUG:
        # static files (images, css, javascript, etc.)
        urlpatterns += patterns('',(r'^resources/(?P<path>.*)$',
                                    'django.views.static.serve',
                                    {'document_root': settings.MEDIA_ROOT}))
