# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions


'''class LoginForm(forms.Form):
        nome = forms.CharField(required=True)
        #senha = forms.CharField(required=True)
        senha = forms.PasswordInput()

        def is_valid(self):
        	valid = True

        	if not super(LoginForm, self).is_valid():
        		self.adiciona_erro('Por favor, verifique os dados informados')
        		valid = False

        	user_exists = User.objects.filter(username=self.data['nome']).exists()



        	if user_exists:
        		self.adiciona_erro('Usuario inexistente')
        		valid = False

        	return valid'''
        

########################################
class AlterarSenhaAtualForm(forms.Form):
        email = forms.EmailField(required=True)
        nova_senha1 = forms.PasswordInput()
        nova_senha2 = forms.PasswordInput()

        '''def is_valid(self):
                valid = True

                if not super(AlterarSenhaAtualForm, self).is_valid():
                    self.adiciona_erro('Senha incompatível')
                    alid = False
                        
                user_exists = User.objects.filter(username=self.data['nome']).exists()

                return valid'''

        def is_valid_Form(self):
            return super(AlterarSenhaAtualForm, self).is_valid()

        def is_valid(self):
            valid = self.is_valid_Form()
            dados = self.dados
            valid_Senha = dados['nova_senha1'] == dados['nova_senha2']
            user_exists = User.objects.filter(email=dados['email']).exists()
            if not user_exists:
                valid = False
                self.add_error(field="email", error="Não há conta registrada com este e-mail")
            if not valid_Senha:
                valid = False
                self.add_error(field=forms.ALL_FIELDS, error="As senhas não conferem")
            return valid


class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True) 
    senha = forms.PasswordInput()
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    def is_valid_from_form(self):
        return super(RegistrarUsuarioForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        user_exists = User.objects.filter(email=self.cleaned_data['email']).exists()
        if user_exists:
            valid = not user_exists
            self.add_error(field="email", error="Já existe uma conta com este email")
        return valid
        
    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList()) 
        errors.append(message)

	
