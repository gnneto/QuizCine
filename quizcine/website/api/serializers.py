from rest_framework import serializers
from website.models import *


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'

class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = '__all__'
        extra_kwargs = {
            'texto': {'validators': []},
        }

class UserPerfilSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = UserProfile
        fields = '__all__'


class RespostaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostaUsuario
        fields = '__all__'


class FilmeRecomendadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmeRecomendado
        fields = '__all__'