# variáveis e constantes

'''
no python não há constantes como em outras linguagens, como o javascript que 
possui o 'const'.

porém existe uma convenção para nomes de constantes que devem ser escritos em
letras maiúsculas 
'''

NOME = "Bruno" #constante
idade = 23 #variavel

print(NOME)

'''
NOME é apenas uma convenção, o interpretador python ainda aceita retribuição de valor
'''

NOME = "Yuri"
print(NOME)

NOME, idade = "Bruno", 23
print(NOME, idade)