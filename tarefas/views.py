from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET'])
def ApiMenu(request):
    api_urls = {
        'Listar Tarefas': '/tarefas',
        'Adicionar Tarefa': '/tarefas',
        'Atualizar': '/att_tarefa/id',
        'Deletar': '/deletar/id',
        'Buscar Pelo titulo': '/?titulo=titulo_name',
        'buscar data_criacao': '/?data_criacao=yyyy-mm-dd',
        'buscar status': '/?status=status',
    }

    return Response(api_urls)


@api_view(['GET', 'POST'])
def tarefas(request):
    if request.method == 'GET':
        lista_de_tarefas = Tarefa.objects.all()
        queryset_serializer = TarefaSerializer(lista_de_tarefas, many=True) #indica que essa é uma listade objetos
        return Response(queryset_serializer.data) #retorna uma lista de dicionários

    if request.method == 'POST':
        tarefa_serializada = TarefaSerializer(data=request.data) #os dados da requisição ficam na propriedade data

        if tarefa_serializada.is_valid():
            tarefa_serializada.save()
            return Response(tarefa_serializada.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) #Os dados não estão corretos

@api_view(['GET','PUT'])
def atualizando_tarefa(request, id):
        #pegando a tarefa pelo id
    tarefa = Tarefa.objects.get(id=id)

    if request.method == 'GET':
        serializer_tarefa = TarefaSerializer(tarefa)
        return Response(serializer_tarefa.data)
    #atualizar as informações serializando

    if request.method == 'PUT':
        serializer_tarefa = TarefaSerializer(tarefa, data=request.data)
        if serializer_tarefa.is_valid():
            serializer_tarefa.save()
            return Response(serializer_tarefa.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def deletar(request, id):
    tarefa = Tarefa.objects.get(id = id)
    tarefa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



