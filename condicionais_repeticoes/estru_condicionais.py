# Estruturas condicionais em python.

'''
Estruturas condicionais em python permitem desvio de fluxo de controle quando determinadas
expressões lógicas são aplicadas.

Estruturas condicionais em python são compostas por: if, else e elif
'''

saldo = 2000
saque = float(input("informe o valor do saque:"))

if saldo >= saque:
  print("saque realizado")

else:
  print("saldo insuficiente")

#===============================


opcao = int(input("informe a opção desejada: [1] para saque, [2] para deposito"))

if opcao == 1:
  '''
  bloco de código para a opção 1
  '''
elif opcao == 2:
  '''
  bloco de código para a opção 2
  '''
else:
  print("opção inválida")
  

#===============================


'''
  if ternário.
  permite escrever uma condiçãos de uma linha
'''

sald = 3000
saq = 4500
status = 'sucess' if sald >= saq else 'error'
print(status)