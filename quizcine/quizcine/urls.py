"""
URL configuration for quizcine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from website.api import viewsets as filmeviewsets


route = routers.DefaultRouter()


route.register(r'filme', filmeviewsets.FilmeViewSet, basename='Filme')
route.register(r'resposta', filmeviewsets.RespostaViewSet, basename='Respostas')
route.register(r'pergunta', filmeviewsets.PerguntaViewSet, basename='Pergunta')
route.register(r'PerfilUsuario', filmeviewsets.UserProfileViewSet, basename='UserProfile')
route.register(r'RespostaUsuario', filmeviewsets.RespostaUsuarioViewSet, basename='RespostaUsuario')
route.register(r'FilmeRecomendado', filmeviewsets.FilmeRecomendadoViewSet, basename='FilmeRecomendado')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(route.urls)),
    path('', include('website.urls')),


    
]
