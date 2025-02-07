from .models import TheUser
from .jwt_helpers import  verificar_jwt

def Procurar_User(request):
    token = request.COOKIES.get('authCookie')
    
    if token:
        payload = verificar_jwt(token) # É verificado se é válido
        user = TheUser.objects.get(id=payload.get('TheUser_ID')) # Se for válido procura o usuário
        if user:
            return user

    return None
