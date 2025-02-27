from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from User.models import TheUser
from User.functions_auxiliaries import Procurar_User
from .models import Post
from .serializers import PostSerializer

def QuantPosts(ext, request):
    User = Procurar_User(request)
    last_object = User.Posts.last()
    
    extension = ext.split('.')[-1]

    if last_object == None:
        return f'1.{extension}'
    else:
        last_object_url = last_object.post.name.split('/')
        number_object_post = (int(last_object_url[-1].split('.')[0]))+1
        
        return f'{number_object_post}.{extension}'
        #for id in range(1, (last_object.id)+2):
        #    try:
        #        id_buscar = Post.objects.get(id=id)
        #        print(f'{id}.{extension[-1]}')
        #    except Post.DoesNotExist:
        #        return f'{id}.{extension[-1]}'
            



# Create your views here.

@api_view(['GET'])
def GetPost(request, id):
    post = Post.objects.get(id=id)
    return redirect(f'/media/{post.post}')

@api_view(['POST'])
def CreatePost(request):
    data = request.data.copy()


    if request.FILES.get('post'):
        post_blob = request.FILES['post']
        nome_arquivo = QuantPosts(post_blob.name, request=request)
        data['post'] = ContentFile(post_blob.read(), name=nome_arquivo)
    
    post = PostSerializer(data=data, context={'request': request})
    print(post)

    if post.is_valid():
        post.save()
        return JsonResponse({'message': 'Post salvo com sucesso'})
    return JsonResponse({'message': 'Não foi possível salvar o post', 'Erro': post.errors})


