# 🎓 AtividadesAPI - Microsserviço de Atividades Acadêmicas

O **AtividadesAPI** é um microsserviço RESTful independente, desenvolvido com **Python e Flask**, responsável por gerenciar atividades acadêmicas vinculadas aos professores. Faz parte da arquitetura de microsserviços integrada ao sistema principal (**DevAPI**), utilizando banco de dados **SQLite** e documentação com **Swagger UI** para testes.

---

## 🚀 Funcionalidades

### 📝 Atividades

- Cadastro de atividades contendo:
  - Título
  - Descrição
  - Professor vinculado (via `professor_id`)
- Listagem completa das atividades registradas.
- Validação de campos obrigatórios.

### 🔗 Integração com Professores

Cada atividade está associada a um professor (`professor_id`), integrando-se ao sistema principal (**DevAPI**).

### 📄 Documentação com Swagger UI

- Interface amigável para testes e visualização de rotas.
- Disponível em: [http://localhost:5002/apidocs](http://localhost:5002/apidocs)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Flask 3.0.2**
- **Flask-SQLAlchemy**
- **Flasgger (Swagger UI)**
- **SQLite**
- **Docker & Docker Compose**

---

## 🐳 Como Rodar com Docker

Clone o repositório:

git clone https://github.com/MATEUS-ANTOVERE-IMPACTA/AtividadesAPI
cd AtividadesAPI
Execute via Docker Compose:

docker-compose up --build
🌐 Acesse a aplicação
Swagger UI: http://localhost:5002/apidocs

API: http://localhost:5002

📂 Estrutura do Projeto

AtividadesAPI/
├── app/
│   ├── controllers/
│   │   └── atividade_controller.py
│   ├── models/
│   │   └── atividade.py
│   ├── config.py
│   ├── extensions.py
│   └── main.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
👨‍🔬 Testes
As rotas podem ser testadas manualmente via Swagger UI, ou utilizando ferramentas como Postman e cURL.

👥 Equipe de Desenvolvimento
Mateus Antovere Silva Rosário | RA: 2401764

Leandro Ferreira Cassemiro Rosa | RA: 2302060

Gabriel Quaglio Monteiro Praça | RA: 2400738
