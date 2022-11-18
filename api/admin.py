from django.contrib import admin
from .models import *

# Lembrando as associações: NomeTabela -> Vem do arquivo models.py

class detAutomoveis(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'preco')
    list_display_links = ('id',)
    search_fields = ('modelo','preco',)
    list_per_page = 10

admin.site.register(automoveis, detAutomoveis)

class detCliente(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(cliente, detCliente)

class detConcessionaria(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(concessionaria, detConcessionaria)

class detArea(admin.ModelAdmin):
    list_display = ('id', 'area')
    list_display_links = ('id',)
    search_fields = ('area',)
    list_per_page = 10

admin.site.register(area, detArea) 

class detAlocacao(admin.ModelAdmin):
    list_display = ('id', 'area', 'automaveis', 'concessionaria', 'quantidade')
    list_display_links = ('id',)
    search_fields = ('area',)
    list_per_page = 10

admin.site.register(alocacao, detAlocacao)

class detVenda(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'concessionaria')
    list_display_links = ('id',)
    search_fields = ('cliente',)
    list_per_page = 10

admin.site.register(venda, detVenda)