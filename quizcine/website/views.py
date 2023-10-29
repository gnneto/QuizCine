from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.contrib import messages
from .models import Filme, Pergunta, Resposta, UserProfile
from .forms import CustomLoginForm, UserProfileForm



def cadastro(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'website/cadastro.html')


def contato(request):
    return render(request, 'website/contato.html')


def criadores(request):
    return render(request, 'website/criadores.html')


def index(request):
    return render(request, 'website/index.html')

def sobre(request):
    return render(request, 'website/sobre.html')

@login_required(login_url='login')
def perfil(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    return render(request, 'website/perfil.html', {'user': user, 'userprofile': userprofile})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = CustomLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('perfil')
                else:
                    form.add_error(None, 'Credenciais inválidas. Tente novamente.')
        else:
            form = CustomLoginForm()
        return render(request, 'website/login.html', {'form': form})



# cadastro de usuario
def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST['pNome']
        sobrenome = request.POST['sNome']
        email = request.POST['email']
        senha = request.POST['senha']
        nascimento = request.POST['nasc']
        cell = request.POST['cell']
        nosConheceu = request.POST.get('nosConheceu', '')
        genero = request.POST['genero']

        try:
            usuario = User.objects.create_user(username=email, email=email, password=senha)
            usuario.first_name = nome
            usuario.last_name = sobrenome
            usuario.save()

            UserProfile.objects.create(
                user=usuario,
                nascimento=nascimento,
                cell=cell,
                nosConheceu=nosConheceu,
                genero=genero
            )

            messages.success(request, 'Cadastro realizado.')
            return redirect('login')
        except IntegrityError as e:
            messages.error(request, 'Erro no cadastro. O email já está em uso.')
        except Exception as e:
            messages.error(request, 'Erro no cadastro: ' + str(e))

    return render(request, 'website/cadastro.html')



@login_required
def quiz(request):
    perguntas = Pergunta.objects.all()
    return render(request, 'website/quiz.html', {'perguntas': perguntas})
    
def resultado_quiz(request):
    if request.method == 'POST':
        respostas_selecionadas = list(request.POST.values())[1:]
        filmes_recomendados = Filme.objects.none()
        
        for id_resposta in respostas_selecionadas:
            resposta = Resposta.objects.get(id=id_resposta)
            filmes_recomendados = filmes_recomendados | resposta.filmes.all()
        
        filmes_recomendados = filmes_recomendados.distinct()
        
        return render(request, 'website/resultado_quiz.html', {'filmes': filmes_recomendados})
    

def editar_perfil(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        if hasattr(request.user, 'userprofile'):
            form = UserProfileForm(instance=request.user.userprofile)
        else:
            form = UserProfileForm()

    return render(request, 'website/editar_perfil.html', {'form': form})
