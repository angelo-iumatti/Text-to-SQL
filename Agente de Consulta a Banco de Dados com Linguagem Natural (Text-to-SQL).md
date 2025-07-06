
# Agente de Consulta a Banco de Dados com Linguagem Natural (Text-to-SQL)

Este projeto demonstra a criação de um agente Text-to-SQL que permite a usuários não-técnicos consultarem um banco de dados SQLite usando linguagem natural (português).

## Funcionalidades

- Traduz perguntas em português para consultas SQL.
- Executa consultas SQL em um banco de dados SQLite.
- Retorna os resultados de forma clara para o usuário.

## Estrutura do Projeto

- `database.db`: O arquivo do banco de dados SQLite (gerado após a execução do `populate_db.py`).
- `schema.sql`: Define o esquema do banco de dados (tabelas `clientes`, `produtos`, `vendas`).
- `populate_db.py`: Script Python para criar o banco de dados e populá-lo com dados fictícios.
- `text_to_sql_agent.py`: O script principal que contém a lógica do agente Text-to-SQL usando LangChain e OpenAI.

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto:

1.  **Pré-requisitos:**
    - Python 3.x
    - `pip` (gerenciador de pacotes do Python)

2.  **Configuração do Ambiente:**

    Navegue até o diretório do projeto no seu terminal:
    ```bash
    cd text-to-sql-agent
    ```

3.  **Instalar Dependências:**

    Instale as bibliotecas Python necessárias:
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: O arquivo `requirements.txt` será gerado automaticamente.)*

4.  **Configurar a Chave da API OpenAI:**

    O agente utiliza o modelo GPT da OpenAI. Você precisa definir sua chave da API OpenAI como uma variável de ambiente. Substitua `SUA_CHAVE_OPENAI_AQUI` pela sua chave real:
    ```bash
    export OPENAI_API_KEY="SUA_CHAVE_OPENAI_AQUI"
    ```
    Para tornar isso permanente, você pode adicionar esta linha ao seu arquivo `.bashrc` ou `.zshrc`.

5.  **Criar e Popular o Banco de Dados:**

    Execute o script `populate_db.py` para criar o banco de dados `database.db` e preenchê-lo com dados fictícios:
    ```bash
    python populate_db.py
    ```

6.  **Executar o Agente Text-to-SQL:**

    Agora você pode iniciar o agente. Ele aguardará suas perguntas no terminal:
    ```bash
    python text_to_sql_agent.py
    ```

7.  **Fazer Perguntas:**

    Com o agente em execução, você pode digitar suas perguntas em português. Por exemplo:

    - `Quantos clientes temos em São Paulo?`
    - `Liste todos os produtos com preço acima de 100 reais.`
    - `Quais são os nomes dos clientes que fizeram compras?`
    - `Qual o total de vendas?`

    Para sair do agente, digite `sair`.

## Esquema do Banco de Dados

### Tabela `clientes`
- `id` (INTEGER PRIMARY KEY)
- `nome` (TEXT)
- `cidade` (TEXT)
- `estado` (TEXT)

### Tabela `produtos`
- `id` (INTEGER PRIMARY KEY)
- `nome` (TEXT)
- `preco` (REAL)

### Tabela `vendas`
- `id` (INTEGER PRIMARY KEY)
- `cliente_id` (INTEGER, FOREIGN KEY para `clientes.id`)
- `produto_id` (INTEGER, FOREIGN KEY para `produtos.id`)
- `data_venda` (TEXT)
- `quantidade` (INTEGER)


