from pathlib import Path

ROOT_PATH = Path(__file__).parent

# FileNotFoundError
try:
  file = open('arquivo_inexistente.txt', 'r')
except FileNotFoundError as exc:
  print('Arquivo não encontrado')
  print(exc)


# IsADirectoryError
try:
  file = open(ROOT_PATH / 'novo_diretorio')
except IsADirectoryError as exc:
  print('Não é possivel abrir um diretório')
  print(exc)


#... 