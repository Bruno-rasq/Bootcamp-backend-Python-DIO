"""
  metodos de classe:

  metodos de classe estão ligado a classe e não ao objeto, eles tem acesso ao estado da classe
  pois recebem um parametro que aponta para a classe e não para a estancia do objeto.

  metodos estaticos:

  um metodo estatico não recebe um primeiro argumento explicito, ele tambem é um metodo vinculado
  a classe e não ao objeto da classe. este metodo n~~ao pode acessar ou modificar o estado da classe
  e esta presente numa classe que faz sentido o metodo estar presente na classe
  
"""

class Pessoa:

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @classmethod
  def criar_pessoa(cls, nome, idade):
    return cls(nome, idade)

  @staticmethod
  def maior_idade(idade):
    return idade >= 18
      


p1 = Pessoa("Claudia", 33)
print(p1.nome, p1.idade)

p2 = Pessoa.criar_pessoa("Bruno", 23)
print(p2.nome, p2.idade)

print(Pessoa.maior_idade(p2.idade))