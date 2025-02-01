from django.urls import path
from .views import Cadastrar_User, Entrar_User, Validar_Token
from .views import HomePageHTML, SettingsPageHTML, PerfilPageHTML

urlpatterns = [
    path('', Validar_Token, name='Validar_Token'), # Url Principal da API User
    path('Cadastrar/', Cadastrar_User, name='Cadastrar_User'),
    path('Entrar/', Entrar_User, name='Entrar_User' ),
    path('Home/', HomePageHTML, name='HomePageHTML'),
    path('Settings/', SettingsPageHTML, name='SettingsPageHTML'),
    path('Perfil/', PerfilPageHTML, name='PerfilPageHTML')
] 