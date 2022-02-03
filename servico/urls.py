from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from servico import views
from servico.models import Servico

urlpatterns = patterns('servico.views',
	(r'^novo/$', 'novo_chamado'),
	(r'^(?P<servico_id>\d+)/$', 'chamado'),
)

urlpatterns += patterns('',
	(r'^central/$', 'django.views.generic.date_based.archive_index',
		{'queryset': Servico.objects.filter(status = Servico.ABERTO_STATUS).all(), 'date_field': 'data_atualizacao'}),
)