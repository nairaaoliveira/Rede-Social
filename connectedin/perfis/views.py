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

	if perfil.is_visible:
		return render(request, 'perfil.html', {
            "is_friend": get_perfil_logado.is_friend_of(perfil),
            "has_invited": get_perfil_logado.has_invited(perfil),
            "is_blocked_by": get_perfil_logado.is_blocked_by(perfil),
            "has_blocked": get_perfil_logado.has_blocked(perfil),
            "profile": perfil,
        })
	else:
		return redirect('index')


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


#################

@login_required
def block(request, id):
    current_profile = get_current_profile(request)
    perfil = Perfil.objects.get(id=id)
    previous_page = 'friends' if ('friends' in request.META['HTTP_REFERER']) else 'show_profile'
    current_profile.block(pfl)
    return redirect(previous_page) if previous_page == 'friends' else redirect(previous_page, id=id)

@login_required
def blocks(request):
    current_profile = get_current_profile(request)
    return render(request, 'bloqueios.html', {
        "current_profile": current_profile,
        "blocks": current_profile.blocks_made.all()
    })

@login_required
def remove_block(request, id):
    current_profile = get_current_profile(request)
    perfil = Perfil.objects.get(id=id)
    previous_page = 'blocks' if ('blocks' in request.META['HTTP_REFERER']) else 'show_profile'
    current_profile.remove_block(perfil)
    return redirect(previous_page) if previous_page == 'blocks' else redirect(previous_page, id=id)


@login_required
def convite_perfil(request, id):
    invited_perfil = Perfil.objects.get(id=id)
    current_perfil = get_current_perfil(request)
    current_perfil.invite(invited_profile)
    return redirect('view_convites')


@login_required
def convite_accept(request, invite_id):
    accepted_convite = Convite.objects.get(id=convite_id)
    accepted_convite.accept()
    return redirect('convite')


@login_required
def convite_decline(request, invite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.delete()

@login_required
def view_friends(request):
    current_profile = get_current_profile(request)
    return render(request, 'friends.html', {
        "current_profile": current_profile,
        "friends": current_profile.friends.all()
    })

@login_required
def remover_um_amigo(request, friend_id):
    #current_profile = get_current_profile(request)

    perfil_amigo = Perfil.objects.get(id=amigo_id)
    current_profile.remove_friend(perfil_amigo)
    return redirect('friends')

@login_required
def mudar_superusuario(request, id):
    #current_profile = get_current_profile(request)

    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    if perfil_logado.user.is_superuser:
        is_superuser = perfil.user.is_superuser
        perfil.user.is_superuser = not is_superuser
        print("%s is now superuser (%s)" % (perfil, perfil.user.is_superuser))
        perfil.usuario.save()
    return redirect('exibir', id=id)

@login_required
def desativar_perfil(request, id):
    current_profile = get_current_profile(request)
    if current_profile is Perfil and (current_profile.id == id or current_profile.user.is_superuser):
        perfil = Perfil.objects.get(id=perfil_id)
        perfil.is_visible = False
        perfil.save()
        return redirect('logout')
    return redirect('index')

@login_required
def remover_perfil(request, id):
    current_profile = get_current_profile(request)
    if current_profile is Perfil and (current_profile.id == id or current_profile.user.is_superuser):
        perfil = Perfil.objects.get(id=perfil_id)
        perfil.delete()
        return redirect('logout')
    return redirect('index')


##################

@login_required
def get_perfil_logado(resquest):
	return resquest.user.perfil


###############################################
@login_required
def senha(request):
	senha = Senha.objects.all()
	return render(request, 'alterar_senha_atual.html', {'senhas' : senha, 'senha_atual' : get_nova_senha(request)})

@login_required
def get_nova_senha(resquest):
	return resquest.user.senha
