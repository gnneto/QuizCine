from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.db.utils import IntegrityError
from django.contrib import messages

from .forms import CustomLoginForm

def cadastro(request):
    return render(request, 'website/cadastro.html')


def contato(request):
    return render(request, 'website/contato.html')


def criadores(request):
    return render(request, 'website/criadores.html')


def index(request):
    return render(request, 'website/index.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Credenciais inválidas. Tente novamente.')
    else:
        form = CustomLoginForm()
    return render(request, 'website/login.html', {'form': form})
def sobre(request):
    return render(request, 'website/sobre.html')



# cadastro de usuario
def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST['pNome']
        sobrenome = request.POST['sNome']
        email = request.POST['email']
        senha = request.POST['senha']
        nasciment = request.POST['nasc']
        celular = request.POST['cell']

        try:
            usuario = User.objects.create_user(username=email, email=email, password=senha)
            usuario.first_name = nome
            usuario.last_name = sobrenome
            usuario.save()

            messages.success(request, 'Cadastro realizado.')
            return redirect('index')
        except IntegrityError as e:
            messages.error(request, 'Erro no cadastro. O email já está em uso.')
        except Exception as e:
            messages.error(request, 'Erro no cadastro: ' + str(e))

    return render(request, 'website/cadastro.html')
