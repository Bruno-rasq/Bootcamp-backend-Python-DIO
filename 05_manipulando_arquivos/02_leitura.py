arquivo = open('05_manipulando_arquivos/lorem.txt', 'r')

# print(arquivo.read()) # retorna todo o conteudo do arquivo
# print(arquivo.readline()) # retorna uma linha por vez
# print(arquivo.readlines()) # retorna todas as linhas do arquivo numa lista

for line in arquivo.readline():
  print(line)

arquivo.close()