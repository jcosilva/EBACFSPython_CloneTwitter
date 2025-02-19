# EBACFSPython_CloneTwitter
Curso EBAC Full Stack Python - Clone Twitter (Projeto Final)

# Twitter Clone

Um clone simples do Twitter desenvolvido com Django, oferecendo funcionalidades básicas de rede social com uma interface limpa e intuitiva.

## Visão Geral

Este projeto implementa um clone simplificado do Twitter com as seguintes funcionalidades:
- Sistema de autenticação (cadastro/login)
- Criação e exclusão de tweets
- Feed de atualizações
- Curtidas em tweets
- Sistema de seguidores
- Perfis de usuário
- Busca de usuários

O sistema utiliza um design responsivo com uma paleta de cores em tons pastéis (azul, verde e branco), proporcionando uma experiência agradável em dispositivos de diferentes tamanhos.

## Tecnologias Utilizadas

- **Backend**: Django 5.1.6
- **Banco de Dados**: PostgreSQL
- **Estilização**: CSS personalizado
- **Configuração**: python-decouple para variáveis de ambiente

## Instalação e Execução

### Pré-requisitos

- Python 3.10 ou superior
- Poetry para gerenciamento de dependências
- PostgreSQL

### Instalação Local

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/twitter-clone.git
   cd twitter-clone
   ```

2. Instale as dependências com Poetry:
   ```bash
   poetry install
   ```

3. Configure as variáveis de ambiente:
   Crie um arquivo `.env` na raiz do projeto com:
   ```
   DEBUG=True
   SECRET_KEY=sua-chave-secreta
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/twitter_clone
   ```

4. Execute as migrações:
   ```bash
   poetry run python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   poetry run python manage.py runserver
   ```

6. Acesse o sistema em http://localhost:8000

## Docker

### Executando com Docker Compose

1. Certifique-se de ter Docker e Docker Compose instalados

2. Execute o sistema com Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. Acesse o sistema em http://localhost:8000

### Construindo a Imagem Docker

```bash
docker build -t twitter-clone:latest .
```

## Estrutura do Projeto

```
twitter-clone/
├── twitter_clone/         # Aplicação principal
│   ├── settings.py        # Configurações do Django
│   ├── urls.py            # Rotas da aplicação
│   └── wsgi.py            # Configuração WSGI
├── tweets/                # App de tweets
├── users/                 # App de usuários
├── static/                # Arquivos estáticos
│   └── style.css          # Estilos CSS
├── templates/             # Templates HTML
│   ├── login.html         # Página de login
│   ├── signup.html        # Página de cadastro
│   ├── home.html          # Feed principal
│   ├── create_tweet.html  # Criação de tweets
│   ├── profile.html       # Perfil do usuário
│   └── search_results.html # Resultados de busca
├── .env                   # Variáveis de ambiente
├── Dockerfile             # Configuração Docker
├── docker-compose.yml     # Configuração Docker Compose
├── pyproject.toml         # Configuração do Poetry
└── README.md              # Documentação
```

## Autores

- Julio Silva - E-Mail: silvajulio@hotmail.com
