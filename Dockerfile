# Imagem base
FROM python:3.10-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

# Instalar Poetry e dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        gcc \
        postgresql-client \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s "${POETRY_HOME}/bin/poetry" /usr/local/bin/poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock* ./

# Instalar dependências
RUN poetry install --no-interaction --no-ansi --no-dev

# Copiar o restante do código
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expor a porta
EXPOSE 8000

# Comando para executar o servidor
CMD ["gunicorn", "twitter_clone.wsgi:application", "--bind", "0.0.0.0:8000"]