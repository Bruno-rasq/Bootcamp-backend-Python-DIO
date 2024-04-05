'''
  convenções de python quanto a sua identação:

  4 espaçoes em branco como iniciativa de bloco,
  cada bloco é como se fosse o escopo de uma função
  
'''

def sacar(self, valor: float) -> None:
  if self.saldo >= valor:
    self.saldo -= valor