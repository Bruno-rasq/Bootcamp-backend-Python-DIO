# para abrir e fechar arquivos em python utiliza-se os metodos open() e close()

'''
metodo open()

necessita de dois parametros, o primeiroé o nome do arquivo que queremos abrir
já o segundo é que tipo de interação com o arquivo queremos ter:

r para leitura(read)
w para escrever(write)
a para anexar(attach)
'''
file = open('example.txt', 'r') # para leitura
#file2 = open('example.txt', 'w') # para escrever
#file3 = open('example.txt', 'a') # para anexar mais conteudo no arquivo

file.close()