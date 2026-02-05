from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Crud --> forma de fazer utilizando método
@api_view(['GET', 'POST'])
def listar_usuarios(request):
    if request.method == 'GET':
        queryset = Usuario.objects.all()
        serializers = UsuarioSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = UsuarioSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)
    
# Crud Usuários --> forma de fazer utilizando class
class UsuarioView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDatailView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Crud Imoveis
class ImovelView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ImovelDatailView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

# Crud Contrato
class ContratoView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class ContratoDatailView(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

# Crud Pagamentos
class PagamentoView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class PagamentoDatailView(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer