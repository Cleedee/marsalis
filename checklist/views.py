from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from servico.models import Produto
from checklist.models import Problema, NodeRaiz, NodeTecnico, NodePergunta, Node, NodeRoteiro, CheckList
from checklist.forms import NodeRaizForm, RoteiroForm, PerguntaForm
from checklist.utils import criar_folhas

def produtos(request):
	produtos = Produto.objects.all()
	return render_to_response('checklist/produtos.html',
		locals(),
		context_instance = RequestContext(request)
	)
	
def problemas(request, produto_id):
	produto = Produto.objects.get(id  = produto_id)
	lista = Problema.objects.filter(produto = produto).all()
	return render_to_response('checklist/problemas.html',
		locals(),
		context_instance = RequestContext(request)
	)
	
def problema(request, problema_id):
	problema = Problema.objects.get(id = problema_id)
	try:
		node = CheckList.objects.get(problema = problema)
	except CheckList.DoesNotExist:
		node = None
		form = NodeRaizForm(initial={'problema_id':problema.id,'pergunta':'Eh zirikili?'})
	return render_to_response('checklist/problema.html',
		locals(),
		context_instance = RequestContext(request)
	)
	
def criar_checklist(request):
	if request.method == 'POST':
		form = NodeRaizForm(request.POST)
		if form.is_valid():
			problema = Problema.objects.get(id = form.cleaned_data['problema_id'])
			sim = CheckList()
			sim.tipo = CheckList.TIPO_TECNICO
			sim.save()
			nao = CheckList()
			nao.tipo = CheckList.TIPO_TECNICO
			nao.save()
			raiz = CheckList()
			raiz.tipo = CheckList.TIPO_RAIZ
			raiz.problema = problema
			raiz.pergunta = form.cleaned_data['pergunta']
			raiz.node_sim = sim
			raiz.node_nao = nao
			raiz.save()
			request.user.message_set.create(
				message='Pergunta criada com sucesso.'
			)
	return HttpResponseRedirect('/checklist/problema/%d' % problema.id)
	
def criar_roteiro(request, node_id = None, resposta = None):
	if request.method == 'POST':
		form = RoteiroForm(request.POST)
		if form.is_valid():
			pai = CheckList.objects.get(id = form.cleaned_data['pai_id'])
			roteiro = CheckList()
			roteiro.privativo = form.cleaned_data['privativo']
			roteiro.texto = form.cleaned_data['texto']
			roteiro.tipo = CheckList.TIPO_ROTEIRO
			if form.cleaned_data['resposta'] == 'SIM':
				pai.node_sim = roteiro
			else:
				pai.node_nao = roteiro
			roteiro.save()
			pai.save()
			request.user.message_set.create(
				message='Roteiro cadastrado.'
			)
			return HttpResponseRedirect('/checklist')
	else:
		node = CheckList.objects.get(id = node_id)
		form = RoteiroForm(initial={'pai_id':node.id,'resposta': resposta,})
		return render_to_response('checklist/roteiro.html',
			locals(),
			context_instance = RequestContext(request))
	
def criar_pergunta(request, node_id = None, resposta = None):
	node = CheckList.objects.get(id = node_id)
	nova_pergunta = CheckList()
	nova_pergunta.tipo = CheckList.TIPO_PERGUNTA
	sim, nao = criar_folhas()
	nova_pergunta.node_sim = sim
	nova_pergunta.node_nao = nao
	nova_pergunta.save()
	if resposta == 'SIM':
		node.node_sim.delete()
		node.node_sim = nova_pergunta
		node.save()
	else:
		node.node_nao.delete()
		node.node_nao = nova_pergunta
		node.save()
	request.user.message_set.create(message='Pergunta criada com sucesso.')
	return HttpResponseRedirect('/checklist/')