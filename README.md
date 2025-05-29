# 🎓 AtividadesAPI - Microsserviço de Atividades Acadêmicas

# O **AtividadesAPI** é um microsserviço RESTful independente, desenvolvido com **Python + Flask**, responsável por gerenciar as **atividades vinculadas aos professores**. Faz parte da arquitetura de microsserviços integrada ao sistema principal (**DevAPI**), utilizando **SQLite** como banco de dados e **Swagger** para documentação e testes.

---

## 🚀 Funcionalidades

- 📝 **Atividades**
  - Cadastro de atividades com título, descrição e professor vinculado.
  - Listagem de todas as atividades registradas.
  - Validação de campos obrigatórios.
  
- 🔗 **Integração com Professores**
  - Cada atividade é associada a um `professor_id`, integrando-se conceitualmente ao sistema principal (**DevAPI**).

- 📄 **Swagger**
  - Interface amigável para testes e visualização de documentação.
  - Disponível em: [`/apidocs`](http://localhost:5002/apidocs)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Flask 3.0.2
- Flask-SQLAlchemy
- Flasgger (Swagger UI)
- SQLite
- Docker & Docker Compose

---

## 🐳 Como Rodar com Docker

1. Clone o repositório:
   ```bash
   git clone https://github.com/MATEUS-ANTOVERE-IMPACTA/AtividadesAPI
   cd AtividadesAPI
Inicie o container:

bash
Copiar
Editar
docker-compose up --build
Acesse:

Swagger UI: http://localhost:5002/apidocs

API: http://localhost:5002

📁 Estrutura do Projeto
arduino
Copiar
Editar
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
As rotas podem ser testadas manualmente via Swagger, ou utilizando ferramentas como Postman e cURL.

👥 Desenvolvido por
👤 Mateus Antovere Silva Rosário | RA: 2401764
👤 Leandro Ferreira Cassemiro Rosa | RA: 2302060
👤 Gabriel Quaglio Monteiro Praça | RA: 2400738