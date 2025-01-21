from django.urls import path
from . import views


urlpatterns = [
    # CONTRATOS
    path('contratos', views.ContratosList.as_view(), name='contratos'),
    path('contratos/<int:pk>/<str:cpf>/<str:data_emissao>/<str:estado>', views.ContratosRead.as_view(), name='contratos-read'),
    path('contratos/resumo/<str:cpf>/<str:data_emissao>/<str:estado>', views.ContratosResumo.as_view(), name='contratos-resumo'),

    # PARCELAS
    path('parcelas', views.ParcelaCreate.as_view(), name='parcelas')
]