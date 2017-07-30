from django.conf.urls import url
from usuarios.views import *
#from usuarios.views import RegistrarUsuarioView
#from usuarios.views import AlterarSenhaAtualView
#from django.contrib.auth import views
from . import views

urlpatterns = [
	url(r'^registrar/$', RegistrarUsuarioView.as_view() , name = 'registrar'),
	url(r'^login/$', views.LoginView.as_view(), name = 'login'),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^timeline/$', views.timeline, name="timeline"),
    url(r'^alterar_senha/$', views.AlterarSenhaAtualView.as_view(), name="alterar_senha"),
        #url(r'^alterar_senha/$', views.Alterar_novaSenha.as_view(name='alterar_nova_senha.html'), name="nova_senha")
]
