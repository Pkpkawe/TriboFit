from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TheUser, Profile
from .serializers import TheUserSerializer, ProfileSerializer
from .jwt_helpers import criar_jwt, verificar_jwt
from .functions_auxiliaries import Procurar_User
import json, bcrypt, requests, io, os

# Create your views here.


""" Cadastro e Login do Usuário e, Criação e remoção de Cookie"""
    

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


""" Renderização das Páginas """


@api_view(['GET'])
def TriboFitHTML(request):
    return render(request, 'TriboFit/index.html')

@api_view(['GET'])
def HomePageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/HomePage.html', contexto)

@api_view(['GET'])
def ExplorerPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/ExplorerPage.html', contexto)

@api_view(['GET'])
def MessagePageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/MessagePage.html', contexto)

@api_view(['GET'])
def MessageConversationPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/MessageConversationPage.html', contexto)

@api_view(['GET'])
def CreatePageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/CreatePage.html', contexto)

@api_view(['GET'])
def CreateEditPageHTML(request):
    user = Procurar_User(request)
    id_user = str(user.id)

    contexto = {'user': user, 'post_temp': f'/media/User/{id_user}/temp/post_temp'}
    return render(request, 'User/CreateEditPage.html', contexto)

@api_view(['GET'])
def PerfilPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user, 'followers': user.Profile.myfollowers.count(), 'following': user.Profile.myfollowings.count()}
    return render(request, 'User/PerfilPage.html', contexto)

@api_view(['GET'])
def ServicesPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/ServicesPage.html', contexto)

@api_view(['GET'])
def Services_T_TreinoPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/Services/Services_T_TreinoPage.html', contexto)

@api_view(['GET'])
def Services_T_MinhasFichasPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/Services/Services_T_MinhasFichasPage.html', contexto)

@api_view(['GET'])
def Services_T_ExercíciosPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/Services/Services_T_ExercíciosPage.html', contexto)

@api_view(['GET'])
def Services_A_AlimentosPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/Services/Services_A_AlimentosPage.html', contexto)

@api_view(['GET'])
def Services_A_MinhaDietaPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/Services/Services_A_MinhaDietaPage.html', contexto)

@api_view(['GET'])
def Services_P_ProfissionaisPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/Services/Services_P_ProfissionaisPage.html', contexto)

@api_view(['GET'])
def SettingsPageHTML(request):
    user = Procurar_User(request)
    contexto = {'user': user}
    return render(request, 'User/SettingsPage.html', contexto)


""" Outras Funções """

@api_view(['POST'])
def PreviewCreate(request):
    user = Procurar_User(request)
    id_user = str(user.id)

    if request.FILES.get('image'):
        image = request.FILES['image']

        file = FileSystemStorage(location=f'media/User/{id_user}/temp/')
        filename = file.save('post_temp', image)

        return JsonResponse({'message': 'Arquivo salvo', 'url': f'/media/User/{id_user}/temp/post_temp', 'image': '{image}'})   

    elif request.FILES.get('video'):
        video = request.FILES['video']

        file = FileSystemStorage(location=f'media/User/{id_user}/temp/')
        filename = file.save('post_temp', video)

        return JsonResponse({'message': 'Arquivo salvo', 'url': f'/media/User/{id_user}/temp/post_temp'})
    
    return redirect('/User/Create/')

@api_view(['PATCH'])
def UpdatePerfil(request):
    user = Procurar_User(request)
    profile_id = user.Profile.id
    data = request.data.copy()
    print(user.Profile.image_perfil.name)
    filePath = f'media/User/{user.id}/Image_Profile.{(user.Profile.image_perfil.name).split('.')[-1]}'
    print(filePath)

    if os.path.exists(filePath):
        os.remove(filePath)

    if request.FILES.get('image_perfil'):
        file = request.FILES['image_perfil']
        fileExtension = (file.name).split('.')[-1]
        file.name = f'Image_Profile.{fileExtension}'
        data['image_perfil'] = file

    try:
        profile = Profile.objects.get(id=profile_id)
    except Profile.DoesNotExist:
        return JsonResponse({'message': 'Perfil não encontrado'})
    
    serializer = ProfileSerializer(profile, data=data, partial=True)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Perfil atualizado'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
