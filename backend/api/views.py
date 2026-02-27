from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *

# Crud --> forma de fazer utilizando método
# @api_view(['GET', 'POST'])
# def listar_usuarios(request):
#     if request.method == 'GET':
#         queryset = Usuario.objects.all()
#         serializers = UsuarioSerializer(queryset, many=True)
#         return Response(serializers.data)
#     elif request.method == 'POST':
#         serializers = UsuarioSerializer(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

# ***** ModelViewSet *****
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [IsAuthenticated]

    # Filtro básico
    # def get_queryset(self):
    #     tipo = self.request.query_params.get('tipo')
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)
    #     return self.queryset

    # Filtros declarativos
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.queryset.user)

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    # Filtro básico
    # def get_queryset(self):
    #     status = self.request.query_params.get('status')
    #     tipo = self.request.query_params.get('tipo')

    #     if status:
    #         self.queryset = self.queryset.filter(status=status)
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)
    #     return self.queryset

    # Filtros declarativos
    filter_backends = [DjangoFilterBackend]
    filterset_class = ImovelFilter
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.queryset.user)

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = PagamentoFilter
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.queryset.user)

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ContratoFilter
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.queryset.user)
    

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Usuário criado com sucesso."}, status=status.HTTP_201_CREATED)


class MeView(RetrieveAPIView):
    serializer_class = UsuarioSerializer
    def get_object(self, request):
        perfil, created = Usuario.objects.get_or_create(
            user = self.request.user,
            defaults={
                'nome': self.request.user.username,
                'email': self.request.user.email,
                'tipo': 'USER'
            }
        )
        return perfil

# ***** GENERICS *****
# Crud Usuários --> forma de fazer utilizando class
# class UsuarioView(ListCreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# class UsuarioDatailView(RetrieveUpdateDestroyAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# ***** Crud Imoveis *****
# class ImovelView(ListCreateAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# class ImovelDatailView(RetrieveUpdateDestroyAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# ***** Crud Contrato *****
# class ContratoView(ListCreateAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer

# class ContratoDatailView(RetrieveUpdateDestroyAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer

# ***** Crud Pagamentos *****
# class PagamentoView(ListCreateAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer

# class PagamentoDatailView(RetrieveUpdateDestroyAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer



# ***** APIView *****
# USUARIO
# class UsuarioView(APIView):
#     def get(self, request):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class UsuarioDetailView(APIView):
#     def get_object(self, pk):
#         return Usuario.objects.get(pk=pk)
    
#     def get(self, request, pk):
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         usuario = self.get_object(pk)
#         usuario.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # IMOVEL
# class ImovelView(APIView):
#     def get(self, request):
#         imovels = Imovel.objects.all()
#         serializer = ImovelSerializer(imovels, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ImovelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ImovelDetailView(APIView):
#     def get_object(self, pk):
#         return Imovel.objects.get(pk=pk)
    
#     def get(self, request, pk):
#         imovel = self.get_object(pk)
#         serializer = ImovelSerializer(imovel)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         imovel = self.get_object(pk)
#         serializer = ImovelSerializer(imovel, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         imovel = self.get_object(pk)
#         imovel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # PAGAMENTO
# class PagamentoView(APIView):
#     def get(self, request):
#         pagamentos = Pagamento.objects.all()
#         serializer = PagamentoSerializer(pagamentos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PagamentoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class PagamentoDetailView(APIView):
#     def get_object(self, pk):
#         return Pagamento.objects.get(pk=pk)
    
#     def get(self, request, pk):
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         pagamento = self.get_object(pk)
#         pagamento.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # CONTRATO
# class ContratoView(APIView):
#     def get(self, request):
#         contratos = Contrato.objects.all()
#         serializer = ContratoSerializer(contratos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ContratoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ContratoDetailView(APIView):
#     def get_object(self, pk):
#         return Contrato.objects.get(pk=pk)
    
#     def get(self, request, pk):
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         contrato = self.get_object(pk)
#         contrato.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)