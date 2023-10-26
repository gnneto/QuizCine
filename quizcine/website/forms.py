from django import forms
from .models import UserProfile

class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Senha'
    )
    


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nascimento', 'cell', 'nosConheceu', 'genero', 'foto']