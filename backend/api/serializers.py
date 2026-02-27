from rest_framework import serializers
from .models import Usuario, Imovel, Contrato, Pagamento
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RegisterSerializer(serializers.Serializer):
    username =  serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    nome = serializers.CharField(required=False, allow_blank=True, default='')
    telefone = serializers.CharField(required=False, allow_blank=True, default='')
    tipo = serializers.ChoiceField(choices=Usuario.TIPO_CHOICES)

    def create(self, validated_data):
        nome = validated_data.get('nome', '')
        email = validated_data['email']
        telefone = validated_data.get('telefone', '')
        tipo = validated_data['tipo']

        user = User.objects.create_user(
            username=validated_data['username'],
            email=email,
            password=validated_data['password']
        )

        user.is_staff = False
        user.is_active = True
        user.save()

        Usuario.objects.create(
            user = user,
            nome = nome if nome else user.username,
            email = email,
            telefone = telefone,
            tipo = tipo
        )

        return user

class UsuarioMeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    is_staff = serializers.BooleanField(source='user.is_staff', read_only=True)
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'telefone', 'tipo', 'is_staff']


class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'