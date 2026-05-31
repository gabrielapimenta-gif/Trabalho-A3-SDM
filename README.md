# Sistema Distribuído de Consulta de CEP

## Descrição

Sistema distribuído desenvolvido com Flask, RabbitMQ, Docker e ViaCEP.

## Arquitetura

Usuário
↓
API Flask
↓
ViaCEP
↓
SQLite
↓
RabbitMQ
↓
Worker

## Tecnologias

- Python
- Flask
- SQLAlchemy
- RabbitMQ
- Docker
- Docker Compose
- SQLite

## Como executar

docker compose up --build

## Rotas

### GET

/cep/<cep>

### POST

/cep

{
    "cep":"..."
}

### Histórico

/consultas