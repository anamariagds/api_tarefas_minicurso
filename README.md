# API de Tarefas

Este é um projeto de API REST para gerenciar tarefas. Foi desenvolvido com Django e Django Rest Framework.

## Recursos

- **Listar Tarefas**: Obtém uma lista de todas as tarefas.
- **Adicionar Tarefa**: Adiciona uma nova tarefa.
- **Atualizar Tarefa**: Atualiza uma tarefa existente.
- **Deletar Tarefa**: Remove uma tarefa.
- **Buscar Tarefa**: Busca tarefas por título, data de criação ou status.

## Endpoints

- **Listar Tarefas**: `GET /tarefas`
- **Adicionar Tarefa**: `POST /tarefas`
- **Atualizar Tarefa**: `PUT /att_tarefa/<id>`
- **Deletar Tarefa**: `DELETE /deletar/<id>`

## Instalação

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/anamariagds/api_tarefas_minicurso.git
   cd api_tarefas_minicurso
   ```

2. **Crie um Ambiente Virtual**:
   ```bash
   python -m venv venv
   ```

3. **Ative o Ambiente Virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute as Migrações**:
   ```bash
   python manage.py migrate
   ```

6. **Inicie o Servidor de Desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

   A API estará disponível em `http://127.0.0.1:8000/`.

## Configuração

Certifique-se de que o arquivo `requirements.txt` está atualizado com as dependências necessárias para o projeto. Caso contrário, você pode gerá-lo com:

```bash
pip freeze > requirements.txt
```

## Contribuição

Sinta-se à vontade para contribuir com o projeto! Para isso:

1. **Faça um Fork do Repositório**.
2. **Crie uma Branch para sua Feature**:
   ```bash
   git checkout -b minha-feature
   ```
3. **Faça Commit das Suas Alterações**:
   ```bash
   git commit -am 'Adiciona nova feature'
   ```
4. **Faça Push para a Branch**:
   ```bash
   git push origin minha-feature
   ```
5. **Crie um Pull Request**.


## Contato

Se você tiver dúvidas ou sugestões, entre em contato com [Ana](mailto:gomesabam@gmail.com).
