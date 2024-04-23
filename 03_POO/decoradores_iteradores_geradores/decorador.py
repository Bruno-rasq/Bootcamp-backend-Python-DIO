def meu_decorador(funcao):
  def envelope():
    print("faz algo antes de executar a funcao")
    funcao()
    print("faz algo depois de executar a funcao")


  return envelope

#acucar sintatico
@meu_decorador
def hello_world():
  print('hello_world')

#hello_world = meu_decorador(hello_world)
hello_world()