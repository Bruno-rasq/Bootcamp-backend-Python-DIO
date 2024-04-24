from pathlib import Path

ROOOT_PATH = Path(__file__).parent

# file = open(ROOOT_PATH / 'lorem.txt', 'r')
# file.close()

with open(ROOOT_PATH / 'lorem.txt', 'r') as file: #abre/executa/fecha
  print('abrindo o arquivo')

print(file.read()) #error pois file já foi fechado

# IOError
try:
  with open(ROOOT_PATH / 'lorem.txt', 'r') as file: 
    print('code')
except IOError as exc:
  print(f'nao foi possivel abrir o arquivo {exc}')


try:
  with open(ROOOT_PATH / 'lorem.txt', 'w', encoding='utf-8') as file: 
    file.write('texto texto texto texto...')
except IOError as exc:
  print(f'nao foi possivel abrir o arquivo {exc}')