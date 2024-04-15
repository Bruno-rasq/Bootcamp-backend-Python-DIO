def principal():
  print('executando funcao principal')

  def interna():
    print('executando funcao interna')

  def interna2():
    print('executando funcao interna2')

  interna()
  interna2()

principal()