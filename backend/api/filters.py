import django_filters
from .models import *

class UsuarioFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name = 'nome',
        lookup_expr = 'icontains'
    )

    class Meta:
        model : Usuario
        fields = ['nome',  'tipo']