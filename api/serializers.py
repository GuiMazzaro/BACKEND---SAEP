from rest_framework import serializers
from .models import *

# USADO PARA LER OS DADOS SEM ASSOCIAÇÃO COM OUTRAS TABELAS
class automoveisTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = automoveis
        fields = '__all__'

class clienteTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = cliente
        fields = '__all__'

class concessionariaTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = concessionaria
        fields = '__all__'

class areaTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = area
        fields = '__all__'

class alocacaoTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = alocacao
        fields = '__all__'

class getAlocacaoTable(serializers.ModelSerializer):

    area = areaTable(read_only=True)
    cliente = clienteTable(read_only=True)
    automaveis = automoveisTable(read_only=True)
    concessionaria = concessionariaTable(read_only=True)

    class Meta: 
        many = True
        model = alocacao
        fields = '__all__'

class vendaTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = venda
        fields = '__all__'

class getVendaTable(serializers.ModelSerializer):

    cliente = clienteTable(read_only=True)
    concessionaria = concessionariaTable(read_only=True)

    class Meta: 
        many = True
        model = venda
        fields = '__all__'

class automoveisAreaTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = automoveisArea
        fields = '__all__'

class getAutomoveisAreaTable(serializers.ModelSerializer):

    area = areaTable(read_only=True)
    automaveis = automoveisTable(read_only=True)

    class Meta: 
        many = True
        model = automoveisArea
        fields = '__all__'