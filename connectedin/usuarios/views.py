# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from usuarios.forms import AlterarSenhaAtualForm
from django.contrib.auth.models import User
from perfis.models import Perfil
#from perfis.models import Senha


# Create your views here.

class RegistrarUsuarioView(View):

	template = 'registrar.html'

	def get(self, request, *args, **kwargs): 
		form = RegistrarUsuarioForm()
		return render(request, self.template, {'form': form})

	def post(self, request, *args, **kwargs): 
		form = RegistrarUsuarioForm(request.POST, request.FILES)

		if (form.is_valid()): 
			dados = form.data
			#usuario = User.objects.create_user(nome=dados['nome'].replace(" ", "_").lower(),email=dados['email'],senha=dados['senha'])

			usuario = User.objects.create_user(dados['nome'],dados['email']) 
						   #dados['senha'])

			perfil = Perfil.objects.create(
                nome=dados['nome'],
                telefone=dados['telefone'],
                nome_empresa=dados['nome_empresa'],
                usuario=usuario) 
			perfil.save()
			return redirect('login')
		return render(request, self.template, {'form': form})


	'''def get(self, request):
		return render(request, 'registrar.html')

	def post(self, request):
		form = RegistrarUsuarioForm(request.POST)

		if (form.is_valid()) :
			dados = form.cleaned_data

			usuario = User.objects.create_user(dados['nome'],
						   dados['email'], 
						   dados['senha'])

			perfil = Perfil(nome = usuario.username, 
							nome_empresa = dados['nome_empresa'],
							telefone = dados['telefone'],
							usuario = usuario)
			perfil.save()
			return redirect('index')
		
		return render(request, 'registrar.html', {'form': form})'''

def timeline(request):
	return (request,'timeline.html')

class LoginView(View):
	template = 'timeline.html'

	def get(self,request):
		return render(request,'login.html')

	def post(self,request):
		#form = LoginView(request.POST)

		#return render(request, 'login.html', {'form': form})
		return render(request, 'perfil.html')
		#return render(request, self.template, {'form': form})

		#return redirect('timeline')

	

class LogoutView(View):
	def get(self,request):
		return render(request,'login.html')


class AlterarSenhaAtualView(View):

	template = 'alterar_senha_atual.html'

	def get(self, request, *args, **kwargs): 
		form = AlterarSenhaAtualForm()
		uuid = kwargs['token']
		token = Token.objects.get(uuid=uuid)
		print("Refused password renewal with token ", token)
		if token.is_valid():
			return render(request, self.template, {'form': form})
		else:
			return redirect('esqueci_senha_verif')

	def post(self, request, *args, **kwargs):
		form = AlterarSenhaAtualForm(request.POST)
		if form.is_valid():
			data = form.data
			user = User.objects.get(email=data['email'])
			user.set_password(data['nova_senha2'])
			user.save()
			update_session_auth_hash(request, user)
			return redirect('login')
		else:
			return render(request, self.template, {'form': form})

	def post(self, request):
		form = AlterarSenhaAtualForm(request.POST)

		if (form.is_valid()):
			dados = form.cleaned_data

			senha = Senha(senha = usuario.username, 
        					novasenha = dados['nova_senha'],
        					usuario = usuario)
			senha.save()
			return redirect('index')

		return render(request, 'alterar_senha_atual.html', {'form': form})
