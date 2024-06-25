from rest_framework import generics
from .models import Pessoa
from .serializers import PessoaSerializer

class CadastrarPessoaView(generics.CreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

