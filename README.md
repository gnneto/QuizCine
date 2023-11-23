## Como Começar
Antes de prosseguir, é necessário executar o seguinte comando para garantir que as dependências estejam atualizadas: <br>`pip install --upgrade setuptools`

Siga os passos abaixo para configurar e executar o projeto:
1. Clone o repositório para sua máquina local. `git clone https://github.com/gnneto/QuizCine.git`
2. Configure o ambiente virtual e instale as dependências utilizando `pip install -r requirements.txt`.
3. Execute as migrações do banco de dados com `python manage.py migrate`.
4. Crie um superusuário com `python manage.py createsuperuser`.
5. Inicie o servidor de desenvolvimento com `python manage.py runserver`.

Acesse o site em [http://localhost:8000/](http://localhost:8000/) e a interface administrativa em [http://localhost:8000/admin/](http://localhost:8000/admin/).

# Documentação QuizCine

## Visão Geral

O **QuizCine** é um projeto que combina entretenimento e interatividade ao oferecer aos usuários a oportunidade de explorar e descobrir novos filmes com base em suas preferências. O projeto consiste em um website com recursos de quiz, cadastro de usuários, perfis personalizados e uma API para fornecer informações sobre filmes e interações do usuário.

## Funcionalidades Principais

### 1. Quiz de Filmes

Os usuários têm acesso a um quiz interativo que consiste em perguntas relacionadas a preferências cinematográficas. Com base nas respostas fornecidas, o sistema recomenda filmes correspondentes aos gostos do usuário.

### 2. Cadastro e Perfis de Usuário

O projeto permite que os usuários se cadastrem, criem perfis personalizados e acessem recursos exclusivos, como o histórico de respostas do quiz e a lista de filmes recomendados.

### 3. API de Filmes

O **QuizCine** disponibiliza uma API que fornece informações sobre filmes, incluindo detalhes como título, gênero, avaliação, diretor, data de lançamento, descrição e links relacionados. Além disso, a API oferece endpoints para interações do usuário, como respostas do quiz e filmes recomendados.

## Componentes do Projeto

### 1. Configurações do Django

- **`QuizCine/backend/quizcine/settings.py`**: Configurações principais do Django, como autenticação, banco de dados e middleware.

### 2. API

- **`QuizCine/backend/quizcine/urls.py`**: Define as URLs principais do projeto, incluindo rotas para a interface administrativa do Django e rotas da API.
- **`QuizCine/backend/website/api/serializers.py`**: Serializadores para transformar modelos em formatos que podem ser facilmente renderizados em JSON.
- **`QuizCine/backend/website/api/viewsets.py`**: Viewsets do Django Rest Framework para gerenciar operações CRUD nas entidades do aplicativo.

### 3. Modelos de Dados

- **`QuizCine/backend/website/models.py`**: Define os modelos de dados do aplicativo, como `Filme`, `Pergunta`, `UserProfile`, etc.

### 4. Administração do Django

- **`QuizCine/backend/website/admin.py`**: Registra os modelos no painel administrativo do Django para gerenciamento.

### 5. Visualizações

- **`QuizCine/backend/website/views.py`**: Contém funções de visualizações que definem o comportamento das páginas do aplicativo, como a página inicial, página de perfil, login, cadastro, quiz, etc.
- **`QuizCine/backend/website/forms.py`**: Define formulários do Django para autenticação, cadastro de usuário e edição de perfil.

### 6. URLs

- **`QuizCine/backend/website/urls.py`**: Define as URLs para as páginas do aplicativo e as rotas da API, além de integração com o `drf_yasg` para documentação da API.



## Sobre a API

Acesse a documentação da API em [http://localhost:8000/swagger/](http://localhost:8000/swagger/) ou [http://localhost:8000/redoc/](http://localhost:8000/redoc/) para explorar os endpoints disponíveis.


# Exemplos breve da API

## Swagger

### Acesso a Documentação do Swagger

Acesse [http://localhost:8000/swagger/](http://localhost:8000/swagger/) para explorar interativamente a documentação da API usando o Swagger.

### Exemplo de Consulta: Listagem de Filmes

1. **Endpoint:** `/api/filme/`
2. **Método:** `GET`

#### Descrição:

Retorna uma lista de todos os filmes cadastrados no sistema.

Voce tera as seguintes informacoes como resposta:
```
{
    "id": {1},
    "idFilmeAPI": {1},
    "titulo": "{Titulo}",
    "generos": "{Drama, Terror}",
    "avaliacao": "{10}",
    "diretor": "{Diretor}",
    "data_lancamento": "{1972-03-14}",
    "descricao": "{Descrição}",
    "imagem_url": "{https://imagem_capa.com/do_filme}",
    "links": {
        "PrimeVideo": "https://www.primevideo.com/dp/filme_PrimeVideo",
        "Apple TV": "https://tv.apple.com/br/movie/filme_AppleTv",
        "Netflix": "https://www.netflix.com/br/title/filme_Netflix",
        "Outros": "https://www.outroSite.com/quiz_Cine"
}
```

### Exemplo de Consulta: Detalhes de um Filme Específico

1. **Endpoint:** `/api/filme/{id}/`
2. **Método:** `GET`

#### Descrição:

Retorna detalhes de um filme específico com base no ID fornecido.

#### Parâmetros de Consulta:

- `{id}`: ID do filme desejado.


## Exibição de Filmes na Página de Resultado do Quiz

Na página de resultado do quiz [http://127.0.0.1:8000/resultado_quiz/](http://127.0.0.1:8000/resultado_quiz/) (`frontend/src/templates/website/resultado_quiz.html`), os filmes são exibidos em cartões, e cada cartão contém um botão "Mostrar mais" que, quando clicado, abre um modal com informações detalhadas sobre o filme.

### Geração Dinâmica de Botões de Assistir

Dentro do modal, a geração dinâmica de botões "Assistir" é realizada com base nos links armazenados no banco de dados para cada filme.

```html
<!-- vai verificar se existe um link no atributo -->
{% for nome, url in filme.links.items %}
  {% if url %}
    <a href="{{ url }}" target="_blank" class="btn btn-primary btn-block">{{ nome }}</a>
  {% endif %}
{% endfor %}
```
Para cada link presente no atributo `links` do modelo `Filme`, verifica-se se o link existe (`{% if url %}`) e, em caso afirmativo, é gerado um botão "Assistir" com o nome fornecido no link.

O campo `links` é um dicionário que mapeia nomes de plataformas (por exemplo, "PrimeVideo", "Netflix") para os URLs correspondentes. Os botões de assistir na pagina de resultado do quiz são gerados com base nessas informações.


# Página Catalago (API)
[http://127.0.0.1:8000/filme_lista/](http://127.0.0.1:8000/filme_lista/)  -  `frontend/src/templates/website/catalogo.html`


## Configuração do CSRF Token
O objetivo é garantir que o token CSRF seja enviado corretamente nas requisições POST, PUT e DELETE.

- A página utiliza o jQuery para fazer requisições AJAX à API do projeto.
- A função `$(document).ready` é acionada quando o DOM está completamente carregado.
- `$.ajaxSetup` é usado para configurar opções globais para todas as requisições AJAX futuras.
- `beforeSend` é um callback chamado antes de cada requisição AJAX.


Exemplo em JavaScript (jQuery):
```javascript
$(document).ready(function(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}")
            }
        }
    });
});
```


## Enviar Requisição POST para Adicionar Filme

- Utiliza o método `$.ajax` do jQuery para realizar uma requisição assíncrona.
- O objeto de configuração da requisição inclui:
  - `url`: URL do endpoint da API para adicionar um filme.
  - `type`: Tipo de requisição, neste caso, POST.
  - `data`: Os dados do filme a serem enviados no corpo da requisição. Eles são convertidos para formato JSON usando `JSON.stringify`.
  - `contentType`: Tipo de conteúdo do corpo da requisição, indicando que estamos enviando JSON.
  - `dataType`: Tipo de dado esperado na resposta da requisição, neste caso, JSON.
  - `success`: Função de callback que é executada quando a requisição é bem-sucedida. Exibe um alerta indicando que o filme foi adicionado com sucesso e recarrega a página para exibir o novo filme.



Exemplo em JavaScript (jQuery):
```javascript
$.ajax({
    url: 'http://127.0.0.1:8000/api/filme/',
    type: 'POST',
    data: JSON.stringify({
        idFilmeAPI: idFilmeAPI,
        titulo: titulo,
        generos: generos,
        avaliacao: avaliacao,
        diretor: diretor,
        data_lancamento: data_lancamento,
        descricao: descricao,
        imagem_url: imagem_url,
        links: links
    }),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(result) {
        alert("Filme adicionado com sucesso!");
        location.reload();
    }
});
```