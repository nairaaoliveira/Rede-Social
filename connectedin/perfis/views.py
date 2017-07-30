# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Perfil, Convite, Senha
# Create your views here.

from django.contrib.auth.decorators import login_required, permission_required

@login_required
def index(request):
	perfis = Perfil.objects.all()
	return render(request,'index.html',{'perfis' : perfis , 'perfil_logado' : get_perfil_logado(request)})
@login_required
def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id = perfil_id)
	return render(request,'perfil.html',{'perfil' : perfil, 'perfil_logado' : get_perfil_logado(request)})
@login_required
def convidar(request, perfil_id):
	perfil_convidado = Perfil.objects.get(id = perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_convidado)
	return redirect('index')


@login_required
def aceitar(resquest, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

@login_required
def get_perfil_logado(resquest):
	return resquest.user.perfil


###############################################
@login_required
def senha(request):
	senha = Senha.objects.all()
	return render(request, 'alterar_senha_atual.html', {'senhas' : senha, 'senha_atual' : get_senha_alterada(request)})

@login_required
def get_senha_alterada(resquest):
	return resquest.user.senha
