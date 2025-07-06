## Tarefas do Projeto: Agente de Consulta a Banco de Dados com Linguagem Natural (Text-to-SQL)

### Fase 1: Configuração do ambiente e banco de dados
- [x] Instalar o SQLite (já deve estar disponível no ambiente).
- [x] Criar um diretório para o projeto.

### Fase 2: Criação do schema e população do banco
- [x] Definir o schema do banco de dados (tabelas: clientes, produtos, vendas).
- [x] Criar o script SQL para a criação das tabelas.
- [x] Criar o script Python para popular o banco de dados com dados fictícios.

### Fase 3: Implementação do agente Text-to-SQL com LangChain
- [x] Instalar as bibliotecas necessárias (LangChain, SQLAlchemy, etc.).
- [x] Configurar a conexão com o banco de dados via LangChain.
- [ ] **NOTA**: No arquivo `text_to_sql_agent.py`, substitua `"SUA_CHAVE_OPENAI_AQUI"` pela sua chave real da API OpenAI ou configure-a como uma variável de ambiente `OPENAI_API_KEY`.
- [x] Criar o prompt robusto para o LLM gerar SQL válido e seguro.
- [x] Implementar o SQLDatabaseChain do LangChain.

### Fase 4: Criação da interface de usuário
- [x] Desenvolver uma interface simples no terminal para receber a pergunta do usuário.
- [x] Exibir o resultado da consulta de forma clara.

### Fase 5: Testes e demonstração do sistema
- [x] Realizar testes com diferentes perguntas em linguagem natural.
- [x] Validar a geração e execução das consultas SQL.
- [x] Demonstrar o funcionamento do sistema.

### Fase 6: Entrega dos resultados ao usuário
- [x] Organizar todos os arquivos do projeto.
- [x] Fornecer instruções detalhadas para a execução do projeto.

