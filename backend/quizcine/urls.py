
# django
from django.contrib import admin
from django.urls import path, include

# rest api
from rest_framework import routers
from website.api import viewsets as filmeviewsets


# rotas api
route = routers.DefaultRouter()
route.register(r'filme', filmeviewsets.FilmeViewSet, basename='Filme')

# desativei porq nao vou usar
# route.register(r'resposta', filmeviewsets.RespostaViewSet, basename='Respostas')
# route.register(r'pergunta', filmeviewsets.PerguntaViewSet, basename='Pergunta')
# route.register(r'PerfilUsuario', filmeviewsets.UserProfileViewSet, basename='UserProfile')
# route.register(r'RespostaUsuario', filmeviewsets.RespostaUsuarioViewSet, basename='RespostaUsuario')
# route.register(r'FilmeRecomendado', filmeviewsets.FilmeRecomendadoViewSet, basename='FilmeRecomendado')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('', include('website.urls')),

]
