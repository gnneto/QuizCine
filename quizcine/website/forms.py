from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Senha'
    )
    

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nascimento', 'cell', 'nosConheceu', 'genero', 'foto', 'bioUsuario']