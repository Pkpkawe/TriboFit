from rest_framework import serializers
from .models import TheUser, Profile
from User.functions_auxiliaries import Procurar_User

class TheUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheUser
        fields = ['id', 'name', 'email', 'password', 'telephone', 'birth_date']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = ['id', 'image_perfil', 'type_account', 'description']