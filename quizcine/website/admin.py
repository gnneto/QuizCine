from django.contrib import admin
from .models import Filme, Pergunta, Resposta, UserProfile
# Register your models here.

admin.site.register(Filme)
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(UserProfile)

