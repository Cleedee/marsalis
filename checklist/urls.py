from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from checklist import views

urlpatterns = patterns('checklist.views',
	url(r'^problema/(\d+)/$','problema'),
	url(r'^problemas/(\d+)/$','problemas'),
	url(r'^criar_checklist$','criar_checklist'),
	url(r'^criar_pergunta/(\d+)/(\w+)/$','criar_pergunta'),
	url(r'^criar_roteiro/(\d+)/(\w+)/$','criar_roteiro'),
	url(r'^criar_roteiro$','criar_roteiro'),
	url(r'^$','produtos')
)
