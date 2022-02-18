from django.conf.urls.defaults import *
from django.conf import settings

from servico.models import Servico

from servico import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', views.home),
	(r'^checklist/', include('checklist.urls')),
	(r'^servico/chamado/', include('servico.urls')),
	(r'^entrar/$','django.contrib.auth.views.login',{'template_name':'entrar.html'},'entrar'),
	(r'^sair/$','django.contrib.auth.views.logout',{'template_name':'sair.html'},'sair'),
    (r'^admin/', include(admin.site.urls)),
	(r'^media/(.*)$', 'django.views.static.serve',
		{'document_root' : settings.MEDIA_ROOT }),
)
