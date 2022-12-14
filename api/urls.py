from django.contrib import admin
from django.urls import path

from .views import *

# Lembrando as associações: TabelaAPI -> Vem do arquivo views.py

urlpatterns = [
    path("automoveis/", automoveisAPI.as_view(), name="automoveis"),
    path("automoveis/<int:pk>", automoveisAPI.as_view(), name="automoveisParametros"),

    path("clientes/", clientesAPI.as_view(), name="clientes"),
    path("clientes/<int:pk>", clientesAPI.as_view(), name="clientesParametros"),

    path("concessionaria/", concessionariaAPI.as_view(), name="concessionaria"),
    path("concessionaria/<int:pk>", concessionariaAPI.as_view(), name="concessionariaParametros"),

    path("areas/", areaAPI.as_view(), name="area"),
    path("areas/<int:pk>", areaAPI.as_view(), name="areaParametros"),

    path("alocacao/", alocacaoAPI.as_view(), name="alocacao"),
    path("alocacao/<int:pk>", alocacaoAPI.as_view(), name="alocacaoParametros"),
    path("getalocacao/", GetalocacaoAPI.as_view(), name="getalocacao"),

    path("vendas/", vendaAPI.as_view(), name="vendas"),
    path("vendas/<int:pk>", vendaAPI.as_view(), name="vendasParametros"),
    path("getvendas/", GetVendaAPI.as_view(), name="getvenda"),

    path("automovelarea/", automoveisAreaAPI.as_view(), name="automoveisarea"),
    path("automovelarea/<int:pk>", automoveisAreaAPI.as_view(), name="automoveisarea"),
    path("getautomovelarea/", GetautomoveisAreaAPI.as_view(), name="getautomovelarea"),

]
