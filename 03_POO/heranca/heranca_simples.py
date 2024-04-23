class veiculo:
  def __init__(self, cor, placa, rodas):
    self.cor = cor
    self.placa = placa
    self.rodas = rodas

  def ligar_motor(self):
    print('ligando motor')

class motocicleta(veiculo):
  pass

class carro(veiculo):
  pass

class caminhao(veiculo):
  
  def __init__(self, cor, placa, rodas):
    super().__init__(cor, placa, rodas)
    self.capacidade_carga = 0
    
  def possue_carga(self):
    if self.capacidade_carga > 0:
      return True
  

  def inserir_carga(self, peso):
    self.capacidade_carga += peso
    
  pass

moto = motocicleta("preto", "2020BHA", 2)
moto.ligar_motor()

c1 = carro("branco", "xd3345", 4)
c1.ligar_motor()

c2 = caminhao("cinza", "sed345", 16)
c2.ligar_motor()
c2.possue_carga()