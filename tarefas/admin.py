from django.contrib import admin
from .models import Tarefa
# Register your models here.

class Tarefas(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'status', 'data_criacao']
    search_fields = ['tiuto', 'status', 'data_criacao']
    list_filter = ['status', 'data_criacao']
admin.site.register(Tarefa, Tarefas)