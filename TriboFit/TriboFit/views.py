from rest_framework.decorators import api_view
from django.shortcuts import render

@api_view(['GET'])
def IndexHTML(request):
    return render(request, 'TriboFit/index.html')
