from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('contato/', views.contato, name='contato'),
    path('criadores/', views.criadores, name='criadores'),
    path('login/', views.login_view, name='login'),
    path('sobre/', views.sobre, name='sobre'),
    path('cadastrar-usuario/', views.cadastrar_usuario, name='cadastrar_usuario')
]
