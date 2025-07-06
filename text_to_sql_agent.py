
import os
import sqlite3
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage

# Configurar a chave da API OpenAI (substitua pela sua chave real ou use variáveis de ambiente)
# os.environ["OPENAI_API_KEY"] = "SUA_CHAVE_OPENAI_AQUI"

db_path = 'database.db'

def get_sql_agent():
    # Conectar ao banco de dados SQLite
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

    # Inicializar o LLM (usando um placeholder para o modelo, você pode substituir por outro)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Criar o toolkit do banco de dados SQL
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    # Definir o prompt robusto para o LLM
    system_message = SystemMessage(content=(
        "Você é um assistente útil que pode responder a perguntas sobre o banco de dados SQL fornecido.\n"
        "Você deve gerar apenas consultas SQL válidas e seguras. Não execute comandos DELETE, UPDATE ou INSERT.\n"
        "Se a pergunta não puder ser respondida com o esquema do banco de dados, diga que não pode responder.\n"
        "Sempre inclua o nome da tabela ao referenciar colunas para evitar ambiguidades.\n"
        "Por exemplo, para 'clientes', use 'clientes.id', 'clientes.nome', etc.\n"
        "As tabelas disponíveis são: clientes, produtos, vendas. Use-as para responder às perguntas.\n"
        "Ao responder, seja conciso e direto, apresentando apenas a informação solicitada."
    ))

    prompt = PromptTemplate.from_template(
        """Você é um agente de IA especializado em traduzir perguntas em português para consultas SQL e executá-las em um banco de dados SQLite.
        Você tem acesso às seguintes ferramentas:
        
        {tools}
        
        Use o seguinte formato de raciocínio:
        
        Pergunta: a pergunta de entrada que você deve responder
        Pensamento: você deve sempre pensar no que fazer
        Ação: a ação a ser tomada, deve ser uma das [{tool_names}]
        Observação: o resultado da ação
        ... (este Pensamento/Ação/Observação pode se repetir N vezes)
        Pensamento: eu sei a resposta final
        Resposta Final: a resposta final para a pergunta original
        
        Comece!
        
        {system_message}
        
        Pergunta: {input}
        {agent_scratchpad}"""
    )

    # Criar o agente SQL
    agent = create_react_agent(llm=llm, tools=toolkit.get_tools(), prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=toolkit.get_tools(), verbose=True)
    
    return agent_executor

if __name__ == "__main__":
    agent = get_sql_agent()
    print("Agente Text-to-SQL inicializado. Digite sua pergunta (ou 'sair' para encerrar):\n")
    while True:
        user_question = input("Sua pergunta: ")
        if user_question.lower() == 'sair':
            break
        try:
            response = agent.invoke({"input": user_question, "system_message": ""})
            print("Resposta: ", response["output"])
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Por favor, tente novamente ou reformule sua pergunta.")



