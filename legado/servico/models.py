# _*_ coding: latin-1 _*_
from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import datetime


class Usuario(models.Model):
	identificacao = models.CharField(max_length=15,unique=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		"""docstring for __unicode__"""
		return self.usuario
	
class Produto(models.Model):
	descricao = models.CharField(max_length=200,unique=True)
	
	def __unicode__(self):
		return self.descricao
		
	class Meta:
		ordering = ['descricao']

class Servico(models.Model):
	ABERTO_STATUS, EM_ATENDIMENTO_STATUS, PARADO_STATUS, CANCELADO_STATUS, FECHADO_STATUS = range(1,6)
	STATUS_CHOICES = (
		(ABERTO_STATUS, 'ABERTO'),
		(EM_ATENDIMENTO_STATUS, 'EM ATENDIMENTO'),
		(PARADO_STATUS, 'PARADO'),
		(CANCELADO_STATUS, 'CANCELADO'),
		(FECHADO_STATUS, 'FECHADO'),
	)
	
	sumario = models.CharField(max_length=200)
	descricao = models.TextField(blank=True,
		help_text='Descrição detalhada da ordem de serviço. Opcional.')
	cliente = models.ForeignKey(User,related_name='clientes')
	autor = models.ForeignKey(User,related_name='autores')
	responsavel = models.ForeignKey(User,related_name='responsaveis')
	status = models.IntegerField(choices=STATUS_CHOICES, default=ABERTO_STATUS)
	protocolo = models.CharField(max_length=8,editable=False)
	data_inicio = models.DateTimeField(default=datetime.datetime.now, editable=False)
	data_atualizacao = models.DateTimeField(default=datetime.datetime.now, editable=False)
	data_fim = models.DateTimeField(null=True, editable=False)
	produto = models.ForeignKey(Produto)
	# T1
	# T2
	
	class Meta:
		ordering = ['data_atualizacao']
		
	def save(self):
		self.data_atualizacao = datetime.datetime.now()
		if not self.id:
			from random import randint
			randomizar = lambda : randint(11111111,99999999)
			s = True
			while s:
				try:
					protocolo = str(randomizar())
					s = Servico.objects.get(protocolo = protocolo)
				except ObjectDoesNotExist:
					self.protocolo = protocolo
					s = False
		super(Servico, self).save()
	
	def __unicode__(self):
		return self.sumario
		
	def get_absolute_url(self):
		return '/servico/chamado/%d' % self.id
		
class Ocorrencia(models.Model):
	ATENDER, REPASSAR, PENDENCIA_ENCONTRADA, PENDENCIA_RESOLVIDA, DICA, CONTATO, GERAL, FECHAR, CANCELAR = range(1,10)
	TIPO_CHOICES = (
		(ATENDER, 'ATENDER'),
		(REPASSAR, 'REPASSAR'),
		(PENDENCIA_ENCONTRADA, 'PENDENCIA ENCONTRADA'),
		(PENDENCIA_RESOLVIDA, 'PENDENCIA RESOLVIDA'),
		(DICA, 'DICA DE COLEGA'),
		(CONTATO, 'CONTATO COM CLIENTE'),
		(GERAL, 'ACOMPANHAMENTO'),
		(FECHAR, 'FECHAR'),
		(CANCELAR, 'CANCELAR'),
	)	
	
	autor = models.ForeignKey(User)
	servico = models.ForeignKey(Servico)
	data = models.DateTimeField(default=datetime.datetime.now, editable=False)
	tipo = models.IntegerField(choices=TIPO_CHOICES, default=ATENDER)
	descricao = models.TextField(blank=True)
	
	def save(self):
		if self.servico.status == Servico.FECHADO_STATUS or self.servico.status == Servico.CANCELADO_STATUS:
			return 
		if self.tipo == Ocorrencia.ATENDER:
			self.servico.status = Servico.EM_ATENDIMENTO_STATUS
			self.servico.responsavel = self.autor
			self.servico.save()
		elif self.tipo == Ocorrencia.REPASSAR:
			self.servico.status = Servico.PARADO_STATUS
			self.servico.save()
		elif self.tipo == Ocorrencia.PENDENCIA_ENCONTRADA:
			self.servico.status = Servico.PARADO_STATUS
			self.servico.save()
		elif self.tipo == Ocorrencia.PENDENCIA_RESOLVIDA:
			self.servico.status = Servico.EM_ATENDIMENTO_STATUS
			self.servico.save()
		elif self.tipo == Ocorrencia.FECHAR:
			self.servico.status = Servico.FECHADO_STATUS
			self.servico.save()
		elif self.tipo == Ocorrencia.CANCELAR:
			self.servico.status = Servico.CANCELADO_STATUS
			self.servico.save()
		super(Ocorrencia, self).save()