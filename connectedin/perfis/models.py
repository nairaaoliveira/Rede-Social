# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):	
	nome = models.CharField(max_length = 255, null = False)
	telefone = models.CharField(max_length = 15, null = False)
	nome_empresa = models.CharField(max_length = 255, null = True)
	contatos = models.ManyToManyField('self')

	usuario = models.OneToOneField(User, related_name = 'perfil')

	@property
	def email(self):
		return self.usuario.email

	def convidar(self, perfil_convidado):
		convite = Convite(solicitante = self,
			              convidado = perfil_convidado)
		convite.save()

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, 
					 related_name = 'convites_feitos')
	convidado = models.ForeignKey(Perfil, 
		             related_name = 'convites_recebidos')

	def aceitar(self): 
		self.solicitante.contatos.add(self.convidado)
		self.convidado.contatos.add(self.solicitante)
		self.delete()

###############################################
class Senha(models.Model):
        #senhaAtual = models.ForeignKey(Perfil, related_name = 'senha_atual')
        senhaAtual = models.CharField(max_length = 255, null = False)
        novaSenha = models.CharField(max_length = 255, null = False)

