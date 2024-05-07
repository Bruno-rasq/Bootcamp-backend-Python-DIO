import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "clients.db")
cur = con.cursor()

def delete_registro(conexao, cursor, id):
  data = (id,)
  cursor.execute('DELETE FROM clients WHERE id=?;', data)
  conexao.commit()

delete_registro(con, cur, 2)