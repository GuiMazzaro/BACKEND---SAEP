from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

#CLASSE AUTOMOVEIS
class automoveisAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = automaveis.objects.all()
            serializer = automoveisTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = automaveis.objects.get(id=pk)
            serializer = automoveisTable(resultado)
            return Response(serializer.data)

    def post(self, request):

        serializer = automoveisTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        resultado = automaveis.objects.get(id=pk)
        serializer = automoveisTable(resultado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        resultado = automaveis.objects.get(id=pk)       
        resultado.delete()
        return Response({"msg": "Apagado com sucesso"})


#CLASSE CLIENTES
class clientesAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = cliente.objects.all()
            serializer = clienteTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = cliente.objects.get(id=pk)
            serializer = clienteTable(resultado)
            return Response(serializer.data)

    def post(self, request):

        serializer = clienteTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        resultado = cliente.objects.get(id=pk)
        serializer = clienteTable(resultado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        resultado = cliente.objects.get(id=pk)       
        resultado.delete()
        return Response({"msg": "Apagado com sucesso"})


#CLASSE CONCESSIONARIA
class concessionariaAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = concessionaria.objects.all()
            serializer = concessionariaTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = concessionaria.objects.get(id=pk)
            serializer = concessionariaTable(resultado)
            return Response(serializer.data)

    def post(self, request):

        serializer = concessionariaTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        resultado = concessionaria.objects.get(id=pk)
        serializer = concessionariaTable(resultado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        resultado = concessionaria.objects.get(id=pk)       
        resultado.delete()
        return Response({"msg": "Apagado com sucesso"})


#CLASSE AREA
class areaAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = area.objects.all()
            serializer = areaTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = area.objects.get(id=pk)
            serializer = areaTable(resultado)
            return Response(serializer.data)

    def post(self, request):

        serializer = areaTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        resultado = area.objects.get(id=pk)
        serializer = areaTable(resultado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        resultado = area.objects.get(id=pk)       
        resultado.delete()
        return Response({"msg": "Apagado com sucesso"})

#CLASSE ALOCACAO
class alocacaoAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = alocacao.objects.all()
            serializer = alocacaoTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = alocacao.objects.get(id=pk)
            serializer = alocacaoTable(resultado)
            return Response(serializer.data)

    def post(self, request):

        serializer = alocacaoTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        resultado = alocacao.objects.get(id=pk)
        serializer = alocacaoTable(resultado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        resultado = alocacao.objects.get(id=pk)       
        resultado.delete()
        return Response({"msg": "Apagado com sucesso"})

#CLASSE ALOCACAO GET
class GetalocacaoAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = alocacao.objects.all()
            serializer = getAlocacaoTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = alocacao.objects.get(id=pk)
            serializer = getAlocacaoTable(resultado)
            return Response(serializer.data)

#CLASSE VENDA
class vendaAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = venda.objects.all()
            serializer = vendaTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = venda.objects.get(id=pk)
            serializer = vendaTable(resultado)
            return Response(serializer.data)

    def post(self, request):

        serializer = vendaTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        resultado = venda.objects.get(id=pk)
        serializer = vendaTable(resultado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        resultado = venda.objects.get(id=pk)       
        resultado.delete()
        return Response({"msg": "Apagado com sucesso"})

#CLASSE VENDA GET
class GetVendaAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = venda.objects.all()
            serializer = getVendaTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = venda.objects.get(id=pk)
            serializer = getVendaTable(resultado)
            return Response(serializer.data)