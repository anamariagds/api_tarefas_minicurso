# Generated by Django 5.1 on 2024-08-28 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='data_criaco',
            new_name='data_criacao',
        ),
    ]
