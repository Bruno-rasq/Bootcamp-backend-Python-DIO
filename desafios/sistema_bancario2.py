'''
  optimizando o desafio anterior "sistema bancario Versão 1"

  novas features:
  
    - criação de cadastro de usuarios (clientes)
    - criação de uma conta corrente para cada usuario
    - modularização de metodos para saque, deposito e extrato

  saque: 

    A função de saque deve receber os argumentos apenas por nome (keyword only), Sugestão de argumentos
    saldo, valor, extrato, limite numero_saques, limite_saques. Sugestão de retorno saldo e extrato.

  deposito:

    A função de deposito deve receber os argumentos apenas por posição (positional only), Sugestão de
    argumentos: saldo, valor, extrato. Sugestão de retorno saldo e extrato.

  extrato:

    A função de extrato deve receber os argumentos por posição e nomeados (keyword and 
    positional) argumentos posicionais: saldo, argumentos nomeados: extrato.

  OBS: todas as regras de negocio das operações de saque, deposito e extrato do ultimo desafio devem ser
  mantidas


  [ NOVAS FUNÇÔES ]
  

  criar_usuario:

    O programa deve armazenar os usuarios em uma lista, um usuario é composto por: nome, data de nascimento
    CPF, e endereço. O endereço é uma string com o formato: logradouro - numero - bairro - cidade/sigla estado.
    deve ser armazenados somento os numeros de CPF (sem ponto ou traço) 
    Não podemos cadastrar 2 usuarios com o mesmo CPF.

  criar_conta_corrente:

    O programa deve armazenar contas em lista, uma conta é composta por: agencia, numero da conta, usuario.
    o numero da conta é sequencial, iniciando em 1. O numero da agencia é fixo "0001". 
    o usuario pode ter mais de uma conta, mas uma conta pertence a somente um usuario.

'''
# [VARIAVEIS GLOBAIS]

usuarios = []
contas_correntes = []

#[EXEMPLOS DE USUARIO/CONTA]

usuario = { #exemplo de usuario cadastrado
  "nome": 'bruno',
  "NASCIMENTO": '22/07/2001',
  "CPF": '12345678910',
  "endereco": 'rua - numero - bairro - cidade/sigla - estado'
}

conta = { #exemplo de conta corrente
  "agencia": "0001",
  "numero_da_conta": 1,
  "usuario-CPF": '12345678910',
  "senha": 123,
  "saldo": 6000,
  "extrato": ['Deposito de R$ 6000.00']
}

#adicionando elementos as listas de usuarios e contas, para ter algum valor inicial
usuarios.append(usuario)
contas_correntes.append(conta)


#[TELAS]

menu_inicial = f'''
====================================

| Bem vindo ao Sistema Bancário 2.0 |

        [A] - Entrar.
        [B] - Cadastrar.
        [C] - Sair.
        
====================================
'''

menu_cadastro = f'''
====================================

            Cadastro

  [A] - criar uma conta corrente.
  [B] - cadastrar um novo usuário.
  [C] - sair.

====================================
'''

menu_operacional = f'''
====================================
      
      Menu

      [A] - Depositar.
      [B] - Sacar.
      [C] - ver extrato.
      [D] - sair.

====================================
'''


#[METODOS]:

'''
A função de cadastrar novo usuario tem como unico requisito que o CPF não seja repetido.
'''
def cadastrar_novo_usuario():
  global usuarios
  
  nome = input('insira seu nome completo: ')
  data_de_nasc = input('insira sua data de nascimento(exemplo: xx/xx/xxxx): ')
  CPF = input('insira seu CPF(Somente numeros): ')
  endereco = input('insira seu endereço (rua - bairro - cidade/sigla - estado): ')
  
  new_user = {
    "nome": nome,
    "NASCIMENTO": data_de_nasc,
    "CPF": CPF,
    "endereco": endereco,
  }

  #verifica se já existe um usuario com o CPF informado
  for usuario in usuarios:
    if usuario['CPF'] == new_user['CPF']:
      print('CPF já cadastrado.')
      return
    
  usuarios.append(new_user)
  print("novo usuario cadastrado com sucesso!")

'''
A função de cadastrar nova conta corrente tem como requisto somente ser possivel criar nova conta
com CPF de um usuario já cadastrado no sistema.
'''
def cadastrar_nova_conta_corrente():
  global contas_correntes
  global usuarios

  agencia = "0001"
  numero_da_conta = len(contas_correntes) + 1
  usuario_CPF = input('insira o CPF do usuario: ')
  senha = int(input('insira uma senha numerica: '))

  # Verifica se existe algum usuário cadastrado com o CPF informado
  usuario_encontrado = False
  for usuario in usuarios:
      if usuario['CPF'] == usuario_CPF:
          usuario_encontrado = True
          break

  if usuario_encontrado:
      new_conta = {
          "agencia": agencia,
          "numero_da_conta": numero_da_conta,
          "usuario_CPF": usuario_CPF,
          "senha": senha,
          "saldo": 0,
          "extrato": []
      }
      contas_correntes.append(new_conta)
      print(f"Nova conta cadastrada com sucesso!, numero da conta {new_conta['numero_da_conta']}")
  else:
      print("Erro: Usuário não encontrado com o CPF informado.")

'''
requisição de dados necessarios para habilitar operações de conta corrente
modo de execução: verificacao_de_seguranca(conta=conta cpf_conta=cpf, senha=senha)
'''
def verificacao_de_seguranca(*, conta, cpf_conta, senha_conta):
  
  if conta['usuario_CPF'] == cpf_conta and conta['senha'] == senha_conta:
    return True
    
  else:
    print('Acesso a conta negada, senha ou numero de CPF inválidos')
    return False
   
'''
função de deposito utiliza o numero da conta que sera informado pelo usuario como uma forma de buscar
a conta mais rapido na lista de contas correntes, apos buscar a conta antes de concluir a operação
será verificado se os dados de cpf e senha que o usuario passar batem com os da conta.
argumentos devem ser passados no formato de positional only
'''
def deposito(numero_da_conta):
  global contas_correntes
  
  valor = float(input('insira o valor do deposito: '))
  cpf = input('insira seu cpf: ')
  senha = int(input('insira sua senha: '))
  conta = contas_correntes[numero_da_conta - 1]

  verificar_dados = verificacao_de_seguranca(
    conta=conta, 
    cpf_conta=cpf, 
    senha_conta=senha, 
  )

  if verificar_dados == True:
    conta['saldo'] += valor
    conta['extrato'].append(f'Deposito de R$ {valor:.2f}')
    print("deposito realizado com sucesso!")
  else:
    return 

'''
a função de saque utiliza como argumento o numero da conta assim como a função de deposito
já dentro da função é requisitado o valor do saque(positivo apenas), o cpf e senha do usuario,
a função verifica se os dados de cpf e senha que o usuario passar batem com os dados da conta
antes de concluir o saque
argumentos devem ser passado no formato de keywords only, ou seja numero_da_conta=1
'''
def saque(numero_da_conta):
  global contas_correntes
  
  valor = abs(float(input('insira o valor do saque: ')))
  cpf = input('insira seu cpf: ')
  senha = int(input('insira sua senha: '))
  conta = contas_correntes[numero_da_conta - 1]

  verificar_dados = verificacao_de_seguranca(
    conta=conta, 
    cpf_conta=cpf, 
    senha_conta=senha, 
  )

  if verificar_dados == True:
    if conta['saldo'] >= valor:
      if valor <= 500: #500 reais é o limite de saque
        conta['saldo'] -= valor
        conta['extrato'].append(f'Saque de R$ {valor:.2f}')
        print('saque realizado com sucesso!')
      else:
        print('Saque não permitido. valor excedeu o limite de R$500.00')
        return
    else:
      print('saldo insuficiente')
  else:
    return

'''
A função de extrato utiliza o numero da conta e senha do usuario como argumentos,
verifica se os dados de cpf e senha que o usuario passar batem com os dados da conta
antes de concluir a operação e mostrar o historico de transações da conta e o saldo atual
argumentos da função devem ser no formato positional e keyword
'''
def extrato(numero_da_conta, senha):
  global contas_correntes

  conta = contas_correntes[numero_da_conta - 1]

  if conta['senha'] == senha:

    print(f'''

============ EXTRATO ==============
    
CPF: {conta['usuario_CPF']}
Agencia: {conta['agencia']}
numero da conta: {conta['numero_da_conta']}
    
    ''')
    
    for item in conta['extrato']:
      print(item)
      
    print(f'''

Saldo atual: R${conta["saldo"]:.2f}

===================================
    ''')

    
#[TESTES DE METODOS]

# cadastrar_novo_usuario()
# cadastrar_nova_conta_corrente()
# deposito(1)
# saque(numero_da_conta=1)
# extrato(1, senhan=123)


#[FLUXO PRINCIPAL]

'''
menu principal, exibido assim que o programa começar a rodar
'''
def menu_principal():
  while True:
    opcao = input(menu_inicial)

    if opcao == 'a':
      menu_entrar()

    elif opcao == 'b':
      menu_cadastrar()
      
    elif opcao == 'c':
      print('Obrigado por usar nosso sistema')
      break
      
    else:
      print("opcao invalida")

'''
menu operacional, abre assim que o usuario escolher a opcao entrar no menu principal
é nele que as operações de saque, deposito e extrato são realizadas
'''
def menu_entrar():
  while True:
    opcao = input(menu_operacional)

    if opcao == 'a':
      numero = int(input('insira o numero da conta: '))
      deposito(numero)

    elif opcao == 'b':
      numero_da_conta = int(input('insira o numero da conta: '))
      saque(numero_da_conta=numero_da_conta)

    elif opcao == 'c':
      numero_da_conta = int(input('insira o numero da conta: '))
      senha = int(input('insira sua senha: '))
      extrato(numero_da_conta, senha=senha)

    elif opcao == 'd':
      break

    else:
      print("opcao invalida")

'''
menu de cadastro, abre assim que o usuario escolher a opcao cadastrar no menu principal
posibilitando o cadastro de novo usuario e nova conta corrente
'''
def menu_cadastrar():
  while True:
    opcao = input(menu_cadastro)

    if opcao == 'a':
      cadastrar_nova_conta_corrente()
      
    elif opcao == 'b':
      cadastrar_novo_usuario()

    elif opcao == 'c':
      break

    else:
      print("opcao invalida")



# RUN....
menu_principal()