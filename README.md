# API de Atividades

Este microsserviço é responsável pelo controle de atividades acadêmicas, vinculadas ao ID do professor fornecido pela API do Sistema de Gerenciamento.

## Descrição da API

A API de Atividades permite:
- Criar novas atividades acadêmicas associadas a um professor
- Listar todas as atividades cadastradas
- Buscar atividades por ID
- Buscar atividades por ID do professor

Cada atividade contém:
- Título
- Descrição (opcional)
- Data de entrega
- ID do professor responsável
- Data de criação

## Instruções de Execução (com Docker)

### Pré-requisitos
- Docker instalado
- Docker Compose instalado (opcional, para execução com outros serviços)

### Execução Standalone
1. Clone o repositório:
```bash
git clone https://github.com/MATEUS-ANTOVERE-IMPACTA/AtividadesAPI.git
cd AtividadesAPI
```

2. Construa e execute o container:
```bash
docker build -t atividades-api .
docker run -p 5001:5001 atividades-api
```

3. A API estará disponível em: http://localhost:5001

### Execução com Docker Compose (integração completa)
Para executar junto com os outros microsserviços:

```bash
docker-compose up
```

## Arquitetura Utilizada

Este projeto segue o padrão de arquitetura MVC (Model-View-Controller):

- **Model**: Representa os dados e a lógica de negócios
  - `app/models/atividade.py`: Define a estrutura de dados e operações CRUD para atividades

- **Controller**: Gerencia as requisições HTTP e coordena as respostas
  - `app/controllers/atividade_controller.py`: Implementa as rotas da API e a lógica de validação

- **View**: Implementada implicitamente através das respostas JSON da API

Outras características:
- Persistência de dados com SQLite
- API RESTful com suporte aos verbos HTTP GET e POST
- Conteinerização com Docker para facilitar a implantação

## Ecossistema de Microsserviços

Este microsserviço faz parte de um ecossistema composto por três serviços independentes:

1. **Sistema de Gerenciamento** (API principal)
   - Responsável pelo cadastro e gerenciamento de alunos, professores e turmas
   - Fornece IDs de professores que são utilizados por este serviço

2. **Reservas**
   - Gerencia reservas de salas de aula
   - Vinculado ao ID da turma fornecido pela API principal

3. **Atividades** (este serviço)
   - Gerencia atividades acadêmicas
   - Vinculado ao ID do professor fornecido pela API principal

### Integração entre os Serviços

- Este serviço consome dados da API de Sistema de Gerenciamento para validar a existência de professores
- A comunicação entre os serviços é feita via requisições HTTP
- Cada serviço mantém seu próprio banco de dados, seguindo o princípio de desacoplamento de microsserviços
- A integração é baseada em IDs compartilhados, permitindo relacionamentos entre entidades de diferentes serviços

## Endpoints da API

### GET /atividades
Lista todas as atividades cadastradas.

### GET /atividades/{id}
Retorna uma atividade específica pelo ID.

### GET /atividades/professor/{professor_id}
Lista todas as atividades associadas a um professor específico.

### POST /atividades
Cria uma nova atividade.

Exemplo de payload:
```json
{
  "titulo": "Trabalho Final de Programação",
  "descricao": "Implementar um sistema de gerenciamento de biblioteca",
  "data_entrega": "2025-06-30",
  "professor_id": 1
}
```

Campos obrigatórios:
- titulo
- data_entrega
- professor_id
