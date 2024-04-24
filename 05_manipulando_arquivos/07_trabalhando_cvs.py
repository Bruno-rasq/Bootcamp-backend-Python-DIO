import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
COLUNA_ID = 0
COLUNA_NOME = 1

# try:
#   with open(ROOT_PATH / 'data.cvs', 'w', newline='' encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['id', 'nome'])
#     writer.writerow(['01', 'maria'])
#     writer.writerow(['02', 'daniela'])
    
# except IOError as exc:
#   print(f'erro ao criar arquivo! {exc}')


try:
  with open(ROOT_PATH / 'data.cvs', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
      print(f'ID: {row[COLUNA_ID]} - Nome: {row[COLUNA_NOME]}')

except IOError as exc:
  print(f'erro ao criar arquivo! {exc}')


try:
  with open(ROOT_PATH / 'data.cvs', newline='') as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
      print(row['id'], row['nome'])

except IOError as exc:
  print(f'erro ao criar arquivo! {exc}')