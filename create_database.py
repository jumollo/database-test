import sqlite3

# Conectar ao banco de dados (cria se não existir)
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Criar tabela de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT
)
''')

# Confirmar mudanças
conn.commit()

# Fechar conexão
conn.close()

print("Banco de dados e tabela criados com sucesso.")