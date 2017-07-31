from django.conf.urls import url
from perfis import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^perfil/(?P<perfil_id>\d+)$', views.exibir, name = 'exibir'),
	url(r'^perfil/(?P<perfil_id>\d+)/convidar$', views.convidar, name = 'convidar'),   
  	url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar'),	
    #url(r'^profile/(?P<id>\d+)/invite$', views.convite_perfil, name="convite_perfil"),
    url(r'^perfil/(?P<perfil_id>\d+)/remover$', views.remover_perfil, name='remover'),
	url(r'^perfil/(?P<perfil_id>\d+)/desativar$', views.desativar_perfil, name="desativar"),
    url(r'^profile/(?P<perfil_id>\d+)/superusuario$', views.mudar_superusuario, name="mudar_superusuario"),



    url(r'^perfil/(?P<convite_id>\d+)/convite_aceito$', views.convite_accept, name="convite_aceito"),
    url(r'^perfil/(?P<convite_id>\d+)/decline$', views.convite_decline, name="invite_decline"),
    url(r'^perfil/blocks', views.blocks, name="blocks"),
    url(r'^perfil/(?P<id>\d+)/block', views.block, name="block"),
    url(r'^perfil/(?P<id>\d+)/unblock', views.remove_block, name="unblock"),


    #url(r'^convites$', views.views_convite, name="convites"),
    url(r'^friends$', views.view_friends, name="friends"),
    url(r'^friends/(?P<id>\d+)/remove$', views.remover_um_amigo, name="remover_um_amigo"),	 
]


