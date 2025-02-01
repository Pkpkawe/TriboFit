import jwt
import datetime
from django.conf import settings

def criar_jwt(TheUser_ID):
    payload = { # Conteúdo do Token
        'TheUser_ID': TheUser_ID, # ID do Usuário
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7), # Tempo de Expiração
        'iat': datetime.datetime.utcnow() # Data de Criação do Token
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256') # Criando o token
    return token

def verificar_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256']) # Decodificando o Token
        return payload
    except jwt.ExpiredSignatureError:
        return 'Token expirado'
    except jwt.InvalidTokenError:
        return 'Token inválido'