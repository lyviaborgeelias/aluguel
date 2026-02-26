from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):

    TIPO_CHOICES = [
        ('LOCADOR', 'Locador'),
        ('LOCATARIO', 'Locatário')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nome
    
class Imovel(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="imoveis")

    def __str__(self):
        return self.titulo


class Contrato(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='contrato')
    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='locador')
    locatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='locatario')

    def __str__(self):
        return f"Contrato {self.id}"

class Pagamento(models.Model):
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamentos')

    def __str__(self):
        return f"Pagamento {self.id}"

