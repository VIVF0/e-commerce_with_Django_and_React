from django.urls import path
from .views import CadastrarPessoaView

urlpatterns = [
    path('api/cadastrar_pessoa', CadastrarPessoaView.as_view(), name='cadastrar_pessoa'),
    # Adicione outras URLs conforme necessário
]