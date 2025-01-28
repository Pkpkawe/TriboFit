from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TheUser
from .serializers import TheUserSerializer
import json
from .jwt_helpers import criar_jwt, verificar_jwt
# Create your views here.

@api_view(['GET'])
def Validar_Token(request):
    token = request.COOKIES.get('authCookie')
    
    if not token:
        return render(request, 'TriboFit/index.html')

    try:
        payload = verificar_jwt(token)
        user = TheUser.objects.get(id=payload.get('TheUser_ID'))
        if user:
            return redirect('/User/Home')
    except Exception:
        return render(request, 'TriboFit/index.html')

@api_view(['GET'])
def HomePageHTML(request):
    return render(request, 'User/HomePage.html')
    
@api_view(['POST'])
def Cadastrar_User(request):
    user_cadastro = TheUserSerializer(data=request.data)
    
    if user_cadastro.is_valid():
        user_cadastro.save()

        user = TheUser.objects.get(email=user_cadastro.data.get('email'))

        token = criar_jwt(user.id)
        response = JsonResponse({'message': 'Cadastro bem-sucedido',
                                 'Dados': user_cadastro.data}, status=status.HTTP_201_CREATED)
        response.set_cookie(
            'authCookie',
            token,
            httponly=True,
            secure=True,
            samesite='Strict',
            path='/'
        )

        return response
    
    return Response(user_cadastro.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Entrar_User(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    try:
        user = TheUser.objects.get(email=email)

        if password == user.password:
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
