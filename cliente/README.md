# database-test

Este projeto contém um script para criar uma base de dados SQLite com tabelas de clientes.

## Como usar

Execute o script Python:

```
python create_database.py
```

Isso criará um arquivo `clients.db` com as tabelas:
- `clients_pf`: Para clientes pessoa física (campos: id, name, cpf, email, phone, birth_date)
- `clients_pj`: Para clientes pessoa jurídica (campos: id, company_name, cnpj, contact_name, email, phone)