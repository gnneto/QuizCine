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
    imagem_url = models.URLField()
    links = models.JSONField(default=dict) # bom prkl

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
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nascimento = models.DateField()
    cell = models.CharField(max_length=20)
    nosConheceu = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='profile_pics', blank=True)
    bioUsuario = models.TextField(max_length=500, blank=True)
 
    def __str__(self):
        return self.user.username
    

class RespostaUsuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.ForeignKey(Resposta, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} | {self.pergunta.texto} | {self.resposta.texto}'
    

class FilmeRecomendado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} | {self.filme.titulo}'