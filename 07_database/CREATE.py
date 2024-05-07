import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#cria o databse se não existir e se conecta
con = sqlite3.connect(ROOT_PATH / "clients.db") 

# objeto que interagi direto com o database
cursor = con.cursor()

#cria uma tabela clients
cursor.execute('CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')


# INSERTS

# jeito ERRADO. -- propenso a injecao de sql
def insert_errado(conexao, cursor, nome, email):
  cursor.execute(f"INSERT INTO clients (nome, email) VALUES ('{nome}', '{email}')")
  conexao.commit()

# jeito CORRETO.
def insert_one(conexao, cursor, nome, email):
  data = (nome, email)
  cursor.execute("INSERT INTO clients (nome, email) VALUES (?, ?);", data)
  conexao.commit()

insert_one(con, cursor, 'bruno', 'teste@email.com')

def insert_many(conexao, cursor, dados):
  cursor.executemany('INSERT INTO clients (nome, email) VALUES (?, ?)', dados)
  conexao.commit()


list = [
  ("A", "A@gmail.com"),
  ("B", "B@gmail.com"),
  ("C", "C@gmail.com"),
  ("D", "D@gmail.com")
]

insert_many(con, cursor, list)