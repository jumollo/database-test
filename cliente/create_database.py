import sqlite3

# Conectar ao banco de dados (cria se não existir)
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Criar tabela de clientes pessoa física
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients_pf (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    email TEXT,
    phone TEXT,
    birth_date DATE
)
''')

# Criar tabela de clientes pessoa jurídica
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients_pj (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    cnpj TEXT UNIQUE NOT NULL,
    contact_name TEXT,
    email TEXT,
    phone TEXT
)
''')

# Confirmar mudanças
conn.commit()

# Fechar conexão
conn.close()

print("Banco de dados e tabelas criados com sucesso.")
