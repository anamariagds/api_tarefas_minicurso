from django.urls import path
from .views import tarefas, atualizando_tarefa, deletar, ApiMenu

urlpatterns = [
    path('', ApiMenu, name="ApiMen"),
    path('tarefas/', tarefas, name="tarefas"),
    path('att_tarefa/<int:id>/', atualizando_tarefa, name="att_tarefa"),
    path('deletar/<int:id>/', deletar, name="deletar"),
]