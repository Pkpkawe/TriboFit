class ValidarToken:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        from django.shortcuts import redirect
        from .jwt_helpers import verificar_jwt
        from .models import TheUser
        

        token = request.COOKIES.get('authCookie') # Procura o Cookie "authCookie"
    
        if request.path in ['/User/', '/User/Cadastrar/', '/User/Entrar/']:
            try:
                if token:
                    payload = verificar_jwt(token) # É verificado se é válido
                    user = TheUser.objects.get(id=payload.get('TheUser_ID')) # Se for válido procura o usuário
                    if user:
                        return redirect('/User/Home/')
                else: raise
            except:
                return self.get_response(request)
        
        if not token: # Caso não Existir o Cookie Retorna a Página de Cadastro e Login
            return redirect('/User/')
        
        try: # Caso o Cookie exista
            payload = verificar_jwt(token) # É verificado se é válido
            user = TheUser.objects.get(id=payload.get('TheUser_ID')) # Se for válido procura o usuário
            if user: # Se o usuário Existir Retorna a Página de Início
                return self.get_response(request)
            else: raise
        except:
            return redirect('/User/')
        
class PostTemp:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        from django.shortcuts import redirect
        import os
        from .functions_auxiliaries import Procurar_User

        try:
            user = Procurar_User(request)
            id_user = str(user.id)

            if os.path.exists(f'media/User/{id_user}/temp/post_temp'):
                if request.path not in ['/User/Create/Edit/', f'/media/User/{id_user}/temp/post_temp']:
                    os.remove(f'media/User/{id_user}/temp/post_temp')
            elif request.path == '/User/Create/Edit/':
                return redirect('/User/Create/')
            return self.get_response(request)
        except Exception:
            return self.get_response(request)