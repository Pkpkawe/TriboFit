from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TheUser
from .serializers import TheUserSerializer
import json
import bcrypt
from .jwt_helpers import criar_jwt, verificar_jwt
from .functions_auxiliaries import Procurar_User

# Create your views here.

@api_view(['GET'])
def TriboFitHTML(request):
    return render(request, 'TriboFit/index.html')
    
@api_view(['POST'])
def Cadastrar_User(request): # Função para Cadastrar Usuário
    data = request.data # Armazena os Dados Enviados

    password = (data.get('password')) # Armazena a Senha Enviada
    hashed = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt()) # Criptografa a Senha
    data['password'] = hashed.decode('UTF-8') # Tira a Formatação da Senha em Bytes

    user_cadastro = TheUserSerializer(data=data) # Transforma os Dados Enviados para Validar

    if user_cadastro.is_valid(): 
        user_cadastro.save() # Salva o Usuário no Banco de Dados

        user = TheUser.objects.get(email=user_cadastro.data.get('email')) # Procura o Usuário no Banco de Dados

        token = criar_jwt(user.id) # Cria um Token para o Usuário
        response = JsonResponse({'message': 'Cadastro bem-sucedido',
                                 'Dados': user_cadastro.data}, 
                                 status=status.HTTP_201_CREATED)
        
        response.set_cookie( # Envia o Cookie para Navegador do Usuário
            'authCookie',
            token,
            httponly=True,
            secure=True,
            samesite='Strict',
            path='/'
        )

        return response
    
    return Response(user_cadastro.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def Entrar_User(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    
    try:
        user = TheUser.objects.get(email=email)
        if bcrypt.checkpw(password.encode('UTF-8'), (user.password).encode('UTF-8')): 
            response = JsonResponse({
                'message': 'Authenticação bem-sucedida',
                'id': user.id 
            }, status=status.HTTP_200_OK)
            
            response.set_cookie(
                'authCookie',
                criar_jwt(user.id),
                httponly=True,
                secure=True,
                samesite='Strict',
                path='/'
            )

            return response

        else:
            return JsonResponse({'Error': 'Credenciais inválidas' }, status=status.HTTP_401_UNAUTHORIZED)
        
    except TheUser.DoesNotExist:
        return JsonResponse({'Error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def Sair(request):
    response = JsonResponse({'Cookie':'O Cookie foi removido'}, status=status.HTTP_200_OK)
    response.delete_cookie('authCookie')
    return response

@api_view(['GET'])
def HomePageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/HomePage.html', contexto)

@api_view(['GET'])
def SettingsPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/SettingsPage.html', contexto)

@api_view(['GET'])
def PerfilPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/PerfilPage.html', contexto)