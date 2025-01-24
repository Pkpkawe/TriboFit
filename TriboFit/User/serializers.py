from rest_framework import serializers
from .models import TheUser

class TheUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheUser
        fields = ['id', 'name', 'email', 'password', 'telephone', 'birth_date']