from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):
    idFilmeAPI = models.IntegerField()
    titulo = models.CharField(max_length=200)
    generos = models.CharField(max_length=100)
    avaliacao = models.CharField(max_length=20)
    diretor = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f'{self.titulo} | {self.generos}'
    


class Pergunta(models.Model):
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    filmes = models.ManyToManyField(Filme)

    def __str__(self):
        return self.texto