# MongoBooks - Sistema de Gerenciamento de Biblioteca

Um sistema profissional de gerenciamento de biblioteca baseado em Python que utiliza o MongoDB para armazenamento de dados. Este projeto demonstra as melhores práticas no desenvolvimento Python, incluindo Programação Orientada a Objetos (POO), injeção de dependência e uma arquitetura de código limpa.

## 🚀 Funcionalidades

- **Gerenciamento de Banco de Dados**: Classes dedicadas para conexão e operações no MongoDB.
- **População de Dados (Seeding)**: Script automatizado para preencher o banco de dados com autores, categorias, livros e pedidos iniciais.
- **Operações Avançadas**: Suporte para operações CRUD (Criar, Ler, Atualizar, Deletar) e consultas complexas (ex: filtrar livros por autor ou categoria).
- **Arquitetura Limpa**: Separação clara entre a lógica do banco de dados, constantes e dados de semente (seed data).

## 🛠️ Tecnologias

- **Python 3.x**
- **PyMongo**: Driver oficial do MongoDB para Python.
- **MongoDB**: Banco de dados NoSQL para armazenamento flexível de dados.

## 📂 Estrutura do Projeto

```text
├── MongoBooks/
│   ├── connect_mongo.py     # Lógica de conexão com MongoDB (POO)
│   ├── mongo_books_db.py    # Classe principal de operações da biblioteca
│   └── interface/           # Interfaces para abstração
├── data/
│   ├── seed_data.py         # Dados iniciais para população do banco
│   └── operations_data.py   # Dados usados nos scripts de demonstração
├── constants.py             # Constantes centralizadas (URIs, Cores, Coleções)
├── insert_documents.py      # Script para popular o banco de dados
├── operations.py            # Script demonstrando CRUD e consultas
└── requirements.txt         # Dependências do projeto
```

## ⚙️ Instalação

1.  **Clone o repositório**:
    ```bash
    git clone <url-do-repositorio>
    cd MongoBooks-Library
    ```

2.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Certifique-se de que o MongoDB está rodando**:
    Verifique se o servidor MongoDB está ativo em `localhost:27017` (ou atualize o arquivo `constants.py` com sua URI personalizada).

## 🖥️ Uso

1.  **Popular o Banco de Dados**:
    Preencha sua biblioteca com os dados iniciais:
    ```bash
    python insert_documents.py
    ```

2.  **Executar Demonstrações**:
    Execute várias operações e consultas na biblioteca:
    ```bash
    python operations.py
    ```

## 📝 Licença

Este projeto foi desenvolvido como um exemplo profissional de integração do MongoDB com Python. Sinta-se à vontade para usar e modificar para seu próprio aprendizado ou projetos.
