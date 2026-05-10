import sqlite3
import os

def test_database_creation():
    # Remove o arquivo de banco se existir
    if os.path.exists('clients.db'):
        os.remove('clients.db')
    
    # Executa o script (simulando)
    exec(open('create_database.py').read())
    
    # Verifica se o banco foi criado
    assert os.path.exists('clients.db')
    
    # Verifica as tabelas
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [t[0] for t in tables]
    assert 'clients_pf' in table_names
    assert 'clients_pj' in table_names
    conn.close()

if __name__ == "__main__":
    test_database_creation()
    print("Teste passou!")