
import sqlite3
from faker import Faker
import random

db_path = 'database.db'

def create_tables():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open('schema.sql', 'r') as f:
        schema = f.read()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

def populate_data(num_clientes=50, num_produtos=20, num_vendas=200):
    fake = Faker('pt_BR')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Populate clientes
    clientes_ids = []
    for _ in range(num_clientes):
        nome = fake.name()
        cidade = fake.city()
        estado = fake.state_abbr()
        cursor.execute("INSERT INTO clientes (nome, cidade, estado) VALUES (?, ?, ?)", (nome, cidade, estado))
        clientes_ids.append(cursor.lastrowid)

    # Populate produtos
    produtos_ids = []
    for _ in range(num_produtos):
        nome = fake.word().capitalize() + ' ' + fake.color_name()
        preco = round(random.uniform(10.0, 500.0), 2)
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
        produtos_ids.append(cursor.lastrowid)

    # Populate vendas
    for _ in range(num_vendas):
        cliente_id = random.choice(clientes_ids)
        produto_id = random.choice(produtos_ids)
        data_venda = fake.date_between(start_date='-1y', end_date='today').isoformat()
        quantidade = random.randint(1, 5)
        cursor.execute("INSERT INTO vendas (cliente_id, produto_id, data_venda, quantidade) VALUES (?, ?, ?, ?)",
                       (cliente_id, produto_id, data_venda, quantidade))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    populate_data()
    print(f"Banco de dados '{db_path}' criado e populado com dados fictícios.")


