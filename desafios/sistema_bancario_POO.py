'''
  DESCRIÇÃO
  
  Neste desafio iremos atualizar a implementação do sistema bancário, para armazenar os 
  dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve 
  seguir o modelo de classes UML.
  
'''

from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
  @property
  @abstractmethod
  def valor(self):
    pass

  @abstractmethod
  def registrar(self, conta):
    pass

class Historico:
  def __init__(self):
    self._transacoes = []

  @property
  def transacoes(self):
    return self._transacoes

  def adicionar_transacao(self, transacao):
    self._transacoes.appen({
      "tipo": transacao.__class__.__name__,
      "valor": transacao.valor,
      "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })
    
class Cliente:
  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []

  def realizar_transacao(self, conta, transacao):
    transacao.registrar(conta)

  def adicionar_conta(self, conta):
    self.contas.append(conta)
    
class Pessoa_fisica(Cliente):
  def __init__(self, CPF, nome, DATA_NASCIMENTO, endereco):
    super().__init__(endereco)
    self._CPF = CPF
    self.nome = nome
    self.DATA_NASCIMENTO = DATA_NASCIMENTO

class Conta:
  def __init__(self, numero_conta, cliente):
    self._saldo = 0
    self._NUMERO_CONTA = numero_conta
    self._AGENCIA = "0001"
    self._CLIENTE = cliente
    self._historico = Historico()


  @classmethod
  def nova_conta(cls, client, numero_conta):
    return cls(client, numero_conta)
    
  @property
  def saldo(self):
    return self._saldo

  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      print("deposito realizado com sucesso!")
    else:
      print("houve um erro, transacao nao pode ser realizada")
    
  
  def sacar(self, valor):
    saldo = self.saldo
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
      print("saldo insuficiente")

    elif valor > 0:
      self._saldo -= valor
      print("saque realizado com sucesso!")
      return True

    else:
      print("operacao falhou!")
      return False

  @property
  def agencia(self):
    return self._AGENCIA

  @property
  def numero_conta(self):
    return self._NUMERO_CONTA

  @property
  def cliente(self):
    return self._CLIENTE

  @property
  def historico(self):
    return self._historico

class Conta_corrente(Conta):
  def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):
    super().__init__(numero_conta, cliente)
    self.limite = limite
    self.limite_saques = limite_saques

  def sacar(self, valor):
    numero_saques = len([
      transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__
    ])

    excedeu_limite = valor > self.limite
    excedeu_saques = numero_saques >= self.limite_saques

    if excedeu_limite:
      print("Limite de saque excedido")
    elif excedeu_saques:
      print("Limite de saques excedido")
    else:
      return super().sacar(valor)

    return False

  def __str__(self):
    return f'''
      Agencia:\t{self.agencia}
      c/c:\t\t{self.numero_conta}
      titular:\t{self.cliente.nome}
    '''

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor

  def registrar(self, conta):
    sucesso_transacao = conta.depositar(self.valor)
    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)

class Saque(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor  

  def registrar(self, conta):
    sucesso_transacao = conta.sacar(self.valor)
    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)