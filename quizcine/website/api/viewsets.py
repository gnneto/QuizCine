from rest_framework import viewsets
from website.models import *
from .serializers import *

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer

class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserPerfilSerializer


class RespostaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RespostaUsuario.objects.all()
    serializer_class = RespostaUsuarioSerializer


class FilmeRecomendadoViewSet(viewsets.ModelViewSet):
    queryset = FilmeRecomendado.objects.all()
    serializer_class = FilmeRecomendadoSerializer