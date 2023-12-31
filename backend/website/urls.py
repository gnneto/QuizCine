from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import index
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="QuizCine API",
      default_version='v1',
      # description="",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="quizcine@equipe.com"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   
)
urlpatterns = [
    # site geral
    path('', index, name='index'),
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
    path('perfil/id_<int:user_id>/', views.profile, name='profile'),
    path('filmes_recomendados/', views.filmes_recomendados, name='filmes_recomendados'),
    path('filme_lista/', views.filme_lista, name='filme_lista'),
    path('is_authenticated/', views.is_authenticated_view, name='is_authenticated'),
    path("conta_teste/", views.conta_teste, name='conta_teste'),
    path("documentacao/", views.documentacao, name='documentacao'),

    # url api
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
