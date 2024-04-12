"""

  como o python é uma linguagem de tipagem dinamica, não é necessario declarar o tipo de variavel
  tambem não há palavra chave para atributos publicos, privados e protegidos.

  o python utiliza por convenção o "_" antes do nome de um atributo para indicar que ele é privado.
  ou simplesmente o nome do atributo para indicar que ele é publico.

  publico: atributos que podem ser acessados fora da classe
  privado: atributos que só podem ser acessados dentro da classe
  
"""

class Conta:
  def __init__(self, agencia, saldo=0):
    self._saldo = saldo
    self.numero_agencia = agencia

  def deposito(self,valor):
    # ...
    self._saldo += valor

  def saque(self, valor):
    # ...
    if valor <= self._saldo:
      self._saldo -= valor

  def mostrar_saldo(self):
    # ...
    return self._saldo

conta1 = Conta("0001")
conta1.deposito(1500)
print(conta1.mostrar_saldo())