from django.urls import path
from .views import Criar_User
from .views import HomePageHTML

urlpatterns = [
    path('', Criar_User, name='Criar_User'),
    path('Home/', HomePageHTML, name='HomePageHTML')
]