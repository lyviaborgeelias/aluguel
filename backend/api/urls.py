from django.urls import path, include
from .views import * #listar_usuarios, UsuarioView, UsuarioDetailView, ImovelView, ImovelDetailView, ContratoView, ContratoDetailView, PagamentoView, PagamentoDetailView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'imoveis', ImovelViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'contratos', ContratoViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('', include(router.urls))
    
    # # Usuários
    # path('usuarios', listar_usuarios),
    # path('users', UsuarioView.as_view()),
    # path('usuario/<int:pk>', UsuarioDetailView.as_view()),

    # # Imóveis
    # path('imoveis', ImovelView.as_view()),
    # path('imovel/<int:pk>', ImovelDetailView.as_view()),

    # # Contrato
    # path('contratos', ContratoView.as_view()),
    # path('contrato/<int:pk>', ContratoDetailView.as_view()),

    # # Pagamentos
    # path('pagamentos', PagamentoView.as_view()),
    # path('pagamento/<int:pk>', PagamentoDetailView.as_view()),
]