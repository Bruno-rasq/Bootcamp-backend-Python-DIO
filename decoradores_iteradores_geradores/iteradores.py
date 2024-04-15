'''
  em python um iterador é um objeto que contem um numero contavel de valores que podem ser iterados,
  isso significa que voce pode percorrer todos os valores. O protocolo do iterador é uma maneira do 
  python fazer uma interação de um objeto que contem dois metodos especiais.

  __iter__() e __next__()
'''

from collections.abc import Iterator


class Iterador:
  def __init__(self, numeros: list[int]):
    self.numeros = numeros
    self.index = 0
  
  def __iter__(self):
    return self

  def __next__(self):
    try:
      numero = self.numeros[self.index]
      self.index += 1
      return numero * 2
    except IndexError:
      raise StopIteration

for i in Iterador(numeros=[10, 40, 50]):
  print(i)