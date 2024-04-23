import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / 'novo_diretorio') criar um novo diretorio no caminho passado
# comentei a linha pois depois que é executado a primeira vez criando o dir, o codigo dá erro.


#criando um arquivo dentro do novo_diretorio
#arquivo = open(ROOT_PATH / 'novo_diretorio/teste.txt', 'w')
#arquivo.close()

# renomeando o arquivo teste.txt para teste2.txt
#os.rename(ROOT_PATH / 'novo_diretorio/teste.txt', ROOT_PATH / 'novo_diretorio/teste_alt.txt')

# deleta o arquivo teste2.txt
#os.remove(ROOT_PATH / 'novo_diretorio/teste_alt.txt')

#movendo o aruivo log para dentro do novo_diretorio
#shutil.move(ROOT_PATH / 'log.txt', ROOT_PATH / 'novo_diretorio/log.txt' )