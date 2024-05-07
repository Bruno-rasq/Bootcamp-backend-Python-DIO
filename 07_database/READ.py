import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "clients.db")
cur = con.cursor()

def select_all(conexao, cursor):
  cursor.execute('SELECT * FROM clients')
  datas = cursor.fetchall()

  print('dados da tabela clients:')
  for data in datas:
    print(data)

  conexao.close()

select_all(con, cur)

def select_one(conexao, cursor, id):
  cursor.execute('SELECT * FROM clients WHERE id=?;', (id,) )
  cliente = cur.fetchone()
  print(cliente)
  conexao.close()

#select_one(con, cur, 1)

def row(cursor, id):
  cursor.row_factory = sqlite3.Row
  cursor.execute('SELECT * FROM clients WHERE id=?;', (id,) )
  return cursor.fetchone()


# cliente = row(cur, 1)
# print(dict(cliente))
# print(cliente['nome'])