from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    identificacao = models.CharField(max_length=15,unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.identificacao


class Produto(models.Model):
	descricao = models.CharField(max_length=200,unique=True)

	def __str__(self):
		return self.descricao

	class Meta:
		ordering = ['descricao']
