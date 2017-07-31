# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid as uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Perfil(models.Model):
	usuario = models.OneToOneField(User, related_name = 'perfil', on_delete=models.CASCADE)

	nome = models.CharField(max_length = 255, null = False)
	telefone = models.CharField(max_length = 15, null = False)
	nome_empresa = models.CharField(max_length = 255, null = True)
	contatos = models.ManyToManyField('self')

	
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

class Token(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    until = models.DateTimeField(null=False)

    def __str__(self):
        return "%s valid until %s" % (self.uuid, self.until)

    def is_valid(self):
        return self.until > timezone.now()

class Senha(models.Model):
        #senhaAtual = models.ForeignKey(Perfil, related_name = 'senha_atual')
        senhaAtual = models.CharField(max_length = 255, null = False)
        novaSenha = models.CharField(max_length = 255, null = False)

