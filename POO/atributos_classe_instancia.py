"""
  Atributos do objeto

  todos os objetos nascem com o mesmo numero de atributos de classe e instancia. Atributos
  de instancia são diferentes para cada objeto(cada objeto tem uma copia) já os atributos de 
  classe são compartilhados entre os objetos
  
"""

class Estudante:
  #atributos de classe
  escola = "DIO"

  #atrib utos de instancia
  def __init__(self, nome, matricula):
    self.nome = nome
    self.nmr_matricula = matricula


bruno = Estudante("bruno", 64874638)
gui = Estudante("guilherme", 457735)
  