arquivo = open('05_manipulando_arquivos/log.txt', 'w')

arquivo.write('Hello World!')
arquivo.writelines(['\n', 'escrevendo', '\n', 'um', '\n', 'novo', '\n', 'texto'])

arquivo.close()