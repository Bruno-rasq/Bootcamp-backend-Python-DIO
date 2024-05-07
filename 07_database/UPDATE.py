import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "clients.db")
cur = con.cursor()

def Update_registro(conexao, cursor, nome, email, id):
  data = (nome, email, id)
  cursor.execute('UPDATE clients SET nome=?, email=? WHERE id=?;', data)
  conexao.commit()

Update_registro(con, cur, 'Bruno', 'email@email.com', 1)
Update_registro(con, cur, 'Heleno', 'email@email.com', 2)