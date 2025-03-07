from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Projetos, Colaboradores, Financiadores, AreasTecnologicas
from .serializers import ProjetosSerializer, ColaboradoresSerializer, FinanciadoresSerializer, AreasTecnologicasSerializer

import json

def index(request):
    
    return render(request, 'sume_lccv/index.html')

@api_view(['GET'])
def get_projetos(request):

    if request.method == 'GET':

        projetos = Projetos.objects.all()

        serializer = ProjetosSerializer(projetos, many = True)
        return Response(serializer.data)
    
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_projetos(request):

    if request.method == 'POST':
        novo_projeto = request.data 
        serializer = ProjetosSerializer(data = novo_projeto)

        if serializer.is_valid( ):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def inativar_por_id(request, pk):

    if request.method == 'POST':

        projeto = get_object_or_404(Projetos, pk = pk)

        if not projeto.ativo:
            return Response({"mensagem": "O projeto ja esta inativo"}, status = status.HTTP_400_BAD_REQUEST)
        
        projeto.ativo = False
        projeto.save()

        return Response({"mensagem": "O projeto foi inativado"}, status = status.HTTP_200_OK)


@api_view(['PATCH'])
def editar_projeto(request, pk):

    if request.method == 'PATCH':

        projeto_editado = get_object_or_404(Projetos, pk = pk)

        serializer = ProjetosSerializer(projeto_editado, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"mensagem": "O projeto foi editado"}, status = status.HTTP_200_OK)
        
        return Response({"mensagem": "Nao foi possivel editar"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_projetos_id(request, pk):

    try:
        projeto = get_object_or_404(Projetos, pk = pk)

    except:
        return Response({"mensagem": "Projeto nao encontrado"}, status = status.HTTP_404_NOT_FOUND)
        

    if request.method == 'GET':
        
        serializer = ProjetosSerializer(projeto)
        return Response(serializer.data)

@api_view(['GET'])
def get_equipe_id(request, pk):

    try:
        projeto = get_object_or_404(Projetos, pk = pk)

    except:
        return Response({"mensagem": "Projeto nao encontrado"}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': 
      
        serializer = ProjetosSerializer(projeto)
        return Response(serializer.data["equipe"], status = status.HTTP_200_OK)
        
@api_view(['PATCH'])
def editar_equipe_projeto(request, pk):

    if request.method == 'PATCH':

        projeto_editado = get_object_or_404(Projetos, pk = pk)

        serializer = ProjetosSerializer(projeto_editado, data = {'equipe': request.data['equipe']}, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({"mensagem": "A equipe foi atualizada"}, status = status.HTTP_200_OK)
        
        return Response({"mensagem": "Nao foi atualizar a equipe"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_todos_colaboradores(request):

    if request.method == 'GET':

        colaboradores = Colaboradores.objects.all()

        serializer = ColaboradoresSerializer(colaboradores, many = True)
        return Response(serializer.data)
    
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cadastra_colaborador(request):

    if request.method == 'POST':

        novo_colaborador = request.data 
        serializer = ColaboradoresSerializer(data = novo_colaborador)

        if serializer.is_valid( ):
            serializer.save()
            return Response({"mensagem": "Novo colaborador cadastrado"}, status = status.HTTP_201_CREATED)
        
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_colaborador_by_id(request, pk):

    try:
        colaborador = get_object_or_404(Colaboradores, pk = pk)

    except:
        return Response({"mensagem": "Colaborador nao encontrado"}, status = status.HTTP_404_NOT_FOUND)
        

    if request.method == 'GET':
        
        serializer = ColaboradoresSerializer(colaborador)
        return Response(serializer.data)

@api_view(['PATCH'])
def editar_colaborador_by_id(request, pk):

    if request.method == 'PATCH':

        colaborador_editado = get_object_or_404(Colaboradores, pk = pk)

        serializer = ColaboradoresSerializer(colaborador_editado, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"mensagem": "Dados do colaborador atualizado"}, status = status.HTTP_200_OK)
        
        return Response({"mensagem": "Nao foi possivel editar"}, status = status.HTTP_400_BAD_REQUEST)
