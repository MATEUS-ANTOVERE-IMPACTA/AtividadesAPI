# AtividadesAPI

Microsserviço para gerenciar atividades vinculadas a professores.

## Funcionalidades
- Criar atividades com título, descrição e professor_id
- Listar todas as atividades

## Execução com Docker
```bash
docker-compose up --build
```

Acesse: `http://localhost:5002/atividades`

## Integração
Este microsserviço depende do ID do professor, fornecido pelo Sistema de Gerenciamento (`DEVAPI`).
