"""
  metodo construtor:

  O metodo construtor é sempre executado quando uma nova instancia da classe é criada
  nesse metodo inicializamos o estado do nosso objeto, para declarar o metodo construtor
  da classe usamos a palavra reservada __init__
  
"""

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade


"""
  metodo destrutor:

  O metodo destrutor é sempre executado quando uma instancia da classe é destruida,
  destrutores em python não são necessário quanto em outras linguagem, como c++ porque
  o python possue um gerenciador de lixo que lida com o armagenamento de memoria automaticamente.
  nome do metodo __del__
  
"""

class Pessoa2:
  def __del__(self):
    print('destruindo o objeto')

c = Pessoa2()
del c

#exemplo
class cachorro:
  def __init__(self, nome, raca) -> None:
    self.nome = nome
    self.raca = raca

  def latir(self):
    print(f"{self.nome} fez AU! Au!")
    
  def __del__(self):
    print('NãOOO!, Não mate o doguinhooo')

dog = cachorro('doguinho', 'pitbull')
dog.latir()