# estruturas de repetição em python

'''
  são estruturas que repetem um bloco de codigo um determinado numero de vezes
  atraves de uma expressão logica

  For:
    o comando for é usado para percorrer um objeto iteravel, faz sentido usa-lo
    quando sabemos o numero exato de vezes que o bloco de codigo deve ser executado.
    
'''

lista = ["txt1", "txt2", "txt3"]

for n in lista: #printa todos os items de lista
  print(n)
  
'''
  for com range, range é uma função built-in que é usada para produzir uma sequencia de 
  numeros inteiros a partir de um intervalo especificado.
'''

for n in range(0, 10): #printa de 0 a 9
  print(n)


# printando a tabuada do 5
for j in range(0, 51, 5): #de 0 ao 50 de 5 em 5
  print(j)


'''
  estrutura de repetição while, é usada quando não sabemos o numero exato de vezes que o bloco
  de codigo deverá ser executado.
'''

op = int(input("escolha uma opção: [1] para saque, [2] para deposito, [0]sair"))

while op != 0:
  
  if op == 1:
    print("saque")
  elif op == 2:
    print("deposito")
  else:
    print("saindo")
    
  op = int(input("escolha uma opção: [1] para saque, [2] para deposito, [0]sair"))



