"""
  na herança, a classe filha herda os metodos da classe pai, no entanto é possivel
  modificar um metodo da classe filha herdada da classe pai. isso é particularmento util
  quado os metodos herdados da classe pai não se encaixam na classe filho.
  
"""

class Passaro:
  def voar():
    print('voando')

class Pardal(Passaro):
  def voar(self):
    #return super().voar()
    print("pardal voando...")

class Avestruz(Passaro):
  def voar(self):
    print('avestruz não voa')

#exemplo ruim do uso de herança para ganhar o metodo voar
class Aviao(Passaro):
  def voar(self):
    print('decolando...')

def plano_de_voa(passaro):
  passaro.voar()

plano_de_voa(Pardal())
plano_de_voa(Avestruz())
plano_de_voa(Aviao())