from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from servico.forms import FormNovoChamado, FormChamado, FormOcorrencia
from servico.models import Servico

@login_required
def home(request):
	servicos = Servico.objects.filter(responsavel=request.user)
	return render_to_response('servico/home.html',locals(), context_instance=RequestContext(request))

@login_required
def chamado(request, servico_id=None):
	if request.method == 'POST':
		form = FormOcorrencia(request.POST)
		if form.is_valid():
			ocorrencia = form.save(commit=False)
			ocorrencia.autor = request.user
			servico = get_object_or_404(Servico,pk=form.cleaned_data['servico_id'])
			ocorrencia.servico = servico
			
			ocorrencia.save()
			request.user.message_set.create(
				message='Ocorrencia cadastrada.'
			)
			return HttpResponseRedirect('/servico/chamado/central')
	else:
		servico = get_object_or_404(Servico,pk=servico_id)
		ocorrencias = servico.ocorrencia_set.all()
		form = FormOcorrencia(initial={'servico_id':servico.id})
	return render_to_response('servico/chamado.html',locals(), context_instance=RequestContext(request))

@login_required
def novo_chamado(request):
	if request.method == 'POST':
		form_novo_chamado = FormNovoChamado(request.POST)
		if form_novo_chamado.is_valid():
			chamado = form_novo_chamado.save(commit=False)
			chamado.cliente = request.user
			chamado.autor = request.user
			chamado.responsavel = request.user
			chamado.save()
			request.user.message_set.create(
				message='Chamado criado com protocolo %s ' % chamado.protocolo
			)
			return HttpResponseRedirect('/servico/chamado/%d' % chamado.id)
	else:		
		form_novo_chamado = FormNovoChamado()
	return render_to_response('servico/novo_chamado.html',locals(), context_instance=RequestContext(request))

def cadastrar_ocorrencia(request):
	if request.method == 'POST':
		form = FormOcorrencia(request.POST)
		if form.is_valid():
			ocorrencia = form.save(commit=False)
			ocorrencia.autor = request.user
			ocorrencia.save()
			request.user.message_set.create(
				message='Ocorrencia cadastrada.'
			)
			return HttpResponseRedirect('servico/chamado/central')