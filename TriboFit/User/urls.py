from django.urls import path
from .views import Cadastrar_User, Entrar_User, TriboFitHTML, Sair
from .views import HomePageHTML, SettingsPageHTML, PerfilPageHTML

urlpatterns = [
    path('', TriboFitHTML, name='TriboFitHTML'), # Url Principal da API User
    path('Cadastrar/', Cadastrar_User, name='Cadastrar_User'),
    path('Entrar/', Entrar_User, name='Entrar_User' ),
    path('Home/', HomePageHTML, name='HomePageHTML'),
    path('Settings/', SettingsPageHTML, name='SettingsPageHTML'),
    path('Perfil/', PerfilPageHTML, name='PerfilPageHTML'),
    path('Sair/', Sair, name='Sair')
] 