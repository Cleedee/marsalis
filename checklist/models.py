# _*_ coding: latin-1 _*_
from django.db import models
from servico.models import Produto

class Problema(models.Model):
	produto = models.ForeignKey(Produto)
	descricao = models.TextField()
	
	def __unicode__(self):
		return self.descricao
		
class CheckList(models.Model):
	TIPO_RAIZ = 1
	TIPO_PERGUNTA = 2
	TIPO_ROTEIRO = 3
	TIPO_TECNICO = 4
	TIPO_CHOICES = {TIPO_RAIZ:'Pergunta Inicial',TIPO_PERGUNTA:'Pergunta',
		TIPO_ROTEIRO:'Roteiro',TIPO_TECNICO:'Sem Roteiro'
		}
	
	tipo = models.IntegerField()
	problema = models.ForeignKey(Problema, null = True)
	pergunta = models.CharField(max_length=200)
	node_sim = models.ForeignKey('self', related_name="lista_sim", null=True)
	node_nao = models.ForeignKey('self', related_name="lista_nao", null=True)
	privativo = models.BooleanField(default=False)
	texto = models.TextField(blank=True)
	
	def tipo_display(self):
		return self.TIPO_CHOICES[self.tipo]	
	
class Node(models.Model):
	
	TIPO_RAIZ = 1
	TIPO_PERGUNTA = 2
	TIPO_ROTEIRO = 3
	TIPO_TECNICO = 4
	TIPO_CHOICES = {TIPO_RAIZ:'Pergunta Inicial',TIPO_PERGUNTA:'Pergunta',
		TIPO_ROTEIRO:'Roteiro',TIPO_TECNICO:'Sem Roteiro'
		}
	
	tipo = models.IntegerField()
	
	def tipo_display(self):
		return self.TIPO_CHOICES[self.tipo]
	

class NodeRaiz(Node):
	problema = models.ForeignKey(Problema)
	pergunta = models.CharField(max_length=200)
	node_sim = models.ForeignKey(Node, related_name="sim_lista")
	node_nao = models.ForeignKey(Node, related_name="nao_lista")
	
class NodePergunta(Node):
	pergunta = models.CharField(max_length=200)
	node_sim = models.ForeignKey(Node, related_name="lista_sim") # problema aqui e 
	node_nao = models.ForeignKey(Node, related_name="lista_nao") # aqui

class NodeRoteiro(Node):
	privativo = models.BooleanField(default=False)
	texto = models.TextField()
	
class NodeTecnico(Node):
	pass
	
# tipos
# raiz 1
# pergunta 2
# roteiro 3
# tecnico 4