from rest_framework import serializers
from .models import Usuario, Imovel, Contrato, Pagamento
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RegisterSerializer(serializers.Serializer):
    # Tabela auth_user
    username =  serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    # Tabela api_usuario
    nome = serializers.CharField(required=False, allow_blank=True, default='')
    telefone = serializers.CharField(required=False, allow_blank=True, default='')
    tipo = serializers.ChoiceField(choices=Usuario.TIPO_CHOICES)

    def create(self, validated_data):
        # Criando na Tabela api_usuario
        nome = validated_data.get('nome', '')
        email = validated_data['email']
        telefone = validated_data.get('telefone', '')
        tipo = validated_data['tipo']
        # Criando na Tabela auth_user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=email,
            password=validated_data['password']
        )

        if tipo == "LOCADOR":
            user.is_staff = True
        else:

            user.is_active = False
        user.is_active = True
        user.is_superuser = False
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
    is_superuser = serializers.BooleanField(source='user.is_superuser', read_only=True)
    is_staff = serializers.BooleanField(source='user.is_staff', read_only=True)
    is_active = serializers.BooleanField(source='user.is_active', read_only=True)
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'telefone', 'tipo','username', 'is_superuser', 'is_staff', 'is_active']


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