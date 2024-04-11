class Bicicleta:
  def __init__(self, cor, ano, valor, modelo):
    self.cor = cor
    self.ano = ano
    self.model = modelo
    self.valor = valor
    
  def buzinar(self):
    print('Plim, plim')
    
  def parar(self):
    print('freando...')
    
  def correr(self):
    print('correer!')

  def get_info(self):
    return f"""
    Modelo: {self.model}
    Ano: {self.ano}
    cor: {self.cor}
    valor: {self.valor}
    """

b1 = Bicicleta('azul', 2020, 500, 'caloi')
b1.correr()
b1.buzinar()
b1.parar()  

print(b1.cor, b1.model, b1.ano, b1.valor)

Bicicleta.correr(b1)
print(b1.get_info())