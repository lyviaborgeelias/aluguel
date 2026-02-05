from django.urls import path
from .views import listar_usuarios, UsuarioView, UsuarioDatailView, ImovelView, ImovelDatailView, ContratoView, ContratoDatailView, PagamentoView, PagamentoDatailView

urlpatterns = [
    # Usuários
    path('usuarios', listar_usuarios),
    path('users', UsuarioView.as_view()),
    path('usuario/<int:pk>', UsuarioDatailView.as_view()),

    # Imóveis
    path('imoveis', ImovelView.as_view()),
    path('imovel/<int:pk>', ImovelDatailView.as_view()),

    # Contrato
    path('contratos', ContratoView.as_view()),
    path('contrato/<int:pk>', ContratoDatailView.as_view()),

    # Pagamentos
    path('pagamentos', PagamentoView.as_view()),
    path('pagamento/<int:pk>', PagamentoDatailView.as_view()),
]