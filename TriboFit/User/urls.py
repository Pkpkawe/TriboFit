from django.urls import path
from .views import Cadastrar_User, Entrar_User, TriboFitHTML, Sair, PreviewCreate, UpdatePerfil
from .views import HomePageHTML, SettingsPageHTML, PerfilPageHTML, ServicesPageHTML, MessagePageHTML, ExplorerPageHTML, CreatePageHTML, Services_T_TreinoPageHTML, Services_T_MinhasFichasPageHTML, Services_T_ExercíciosPageHTML, Services_A_AlimentosPageHTML, Services_A_MinhaDietaPageHTML, Services_P_ProfissionaisPageHTML, CreateEditPageHTML, MessageConversationPageHTML

urlpatterns = [
    path('', TriboFitHTML, name='TriboFitHTML'), # Url Principal da API User
    path('Cadastrar/', Cadastrar_User, name='Cadastrar_User'),
    path('Entrar/', Entrar_User, name='Entrar_User' ),
    path('Sair/', Sair, name='Sair'),

    path('Home/', HomePageHTML, name='HomePageHTML'),
    path('Explorer/', ExplorerPageHTML, name='ExplorerPageHTML'),
    path('Message/', MessagePageHTML, name='MessagePageHTML'),
    path('Message/Conversation/', MessageConversationPageHTML, name='MessageConversationPageHTML'),
    path('Create/', CreatePageHTML, name='CreatePageHTML'),
    path('Create/Edit/', CreateEditPageHTML, name='CreateEditPageHTML'),
    path('Perfil/', PerfilPageHTML, name='PerfilPageHTML'),
    path('Services/', ServicesPageHTML, name='ServicesPageHTML'),
    path('Services/Treino/', Services_T_TreinoPageHTML, name='Services_T_TreinoPageHTML'),
    path('Services/MinhasFichas/', Services_T_MinhasFichasPageHTML, name='Services_T_MinhasFichasPageHTML'),
    path('Services/Exercícios/', Services_T_ExercíciosPageHTML, name='Services_T_ExercíciosPageHTML'),
    path('Services/Alimentos/', Services_A_AlimentosPageHTML, name='Services_A_AlimentosPageHTML'),
    path('Services/MinhaDieta/', Services_A_MinhaDietaPageHTML, name='Services_A_MinhaDietaPageHTML'),
    path('Services/Profissionais/', Services_P_ProfissionaisPageHTML, name='Services_P_ProfissionaisPageHTML'),
    path('Settings/', SettingsPageHTML, name='SettingsPageHTML'),

    path('Create/PreviewCreate/', PreviewCreate, name='PreviewCreate'),
    path('Perfil/Update/', UpdatePerfil, name='UpdatePerfil'),
]