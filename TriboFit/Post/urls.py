from django.urls import path
from .views import GetPost, CreatePost

urlpatterns = [
    path('GetPost/<int:id>/', GetPost, name='GetPost'),
    path('CreatePost/', CreatePost, name='CreatePost'),
]