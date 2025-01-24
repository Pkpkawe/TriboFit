from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TheUser
from .serializers import TheUserSerializer
# Create your views here.

@api_view(['GET'])
def HomePageHTML(request):
    return render(request, 'User/HomePage.html')

@api_view(['POST'])
def Criar_User(request):
    user = TheUserSerializer(data=request.data)
    
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
