'''

  desafio 1 python - sistema bancario

  fomos contratados por um grande banco para desenvolver o seu novo sistema.
  esse banco deseja modernizar as suas operações e para issso escolheu a linguagem python
  para a primeira versão do sistema devemos implementar apenas 3 operações: deposito, saque e extrato.

  Operação de depósito:

    deve ser possivel depósitar valores positivos para a minha conta bancária.  A V1 do projeto trabalha
    com apenas um usuario, dessa forma não precisamos nos preocupar em identificar qual é o numero da agência
    e conta bancária. todos os depositos devem ser armazeem uma variavel e exibidos na operação de extrato.

  Operação de saque:

    o sistema deve permitir realizar 3 saques diarios com limite máximo de R$500,00 por saque. caso o usuário
    não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não sera possivel sacar o dinhiero
    por falta de saldo. todos os saques devem ser armazeem uma variavel e exibidos na operação de extrato.

  Opeeração de extrato:

    essa operação deve listar todos os depositos e saques realizados na conta, No fim da listagem deve ser exibido 
    o saldo atual da conta.

    os valores devem ser exibidos utilizando o formato R$ xxx.xx, por exemplo:

    1500.45 => R$1500.45
  
'''


saldo = 0
extrato = []
total_depositios = 0
total_saques = 0
saques_por_dia = 0 # começa com 0 mas o limite são 3 saques por dia
limite_por_saque = 500

menu = '''
===== menu ======

1 - Deposito
2 - saque
3 - ver extrato
4 - sair.

================
'''


def req_valor():
  valor = float(input('informe o valor: '))
  if valor > 0:
    return valor
  else:
    return req_valor()

def deposito():
  global saldo
  global extrato
  global total_depositios
  valor = req_valor()
  saldo += valor
  extrato.append(f'Deposito de R$ {valor:.2f}')
  total_depositios += 1
  print("deposito realizado com sucesso")

def saque():
  global saldo
  global extrato
  global total_saques
  global saques_por_dia
  global limite_por_saque
  if saques_por_dia <= 2:
    valor = req_valor()
    if valor > saldo:
      print('Saldo insuficiente')
    else:
      if valor > limite_por_saque:
        print(f'Saque não permitido. valor excedeu o limite de R${limite_por_saque:.2f}')
      else:
        saldo -= valor
        extrato.append(f'Saque de R$ {valor:.2f}')
        total_saques += 1
        saques_por_dia += 1
        print("saque realizado com sucesso")
  else:
    print('Limite de saques diarios excedido')

def req_extrato():
  global extrato
  global total_depositios
  global total_saques

  print('======== EXTRATO ========')
  for i in extrato:
    print(i)
  print(f'''
  
  total de depositos executados: {total_depositios}
  total de saques executados:  {total_saques}
  
  Saldo atual: R${saldo:.2f}
  ''')

def sair():
  print('Obrigado por usar nosso sistema')


  
while True:
  opcao = int(input(menu))

  if opcao == 1:
    deposito()

  elif opcao == 2:
    saque()

  elif opcao == 3:
    req_extrato()

  elif opcao == 4:
    sair()
    break

  else:
    opcao = int(input(menu))
  