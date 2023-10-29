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
    link_hbo = models.URLField(blank=True)
    link_primevideo = models.URLField(blank=True)
    link_appletv = models.URLField(blank=True)


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
    foto = models.ImageField(upload_to='profile_pics', default='default.jpg')
 
    def __str__(self):
        return self.user.username