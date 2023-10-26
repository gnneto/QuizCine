from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('contato/', views.contato, name='contato'),
    path('criadores/', views.criadores, name='criadores'),
    path('login/', views.login_view, name='login'),
    path('sobre/', views.sobre, name='sobre'),
    path('cadastrar-usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('perfil/', views.perfil, name='perfil'),
    path('quiz/', views.quiz, name='quiz'),
    path('resultado_quiz/', views.resultado_quiz, name='resultado_quiz'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    
    ]
