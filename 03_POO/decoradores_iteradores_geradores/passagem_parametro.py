def mensagem(nome):
  print('executando mensagem')
  return f'Olá {nome}'

def mensagem_longa(nome):
  print('executando mensagem_longa')
  return f'olá, tudo bem com voce {nome}'

def executar(funcao, nome):
  print('executando funcoes')
  return funcao(nome)

print(executar(mensagem, 'Bruno'))
print(executar(mensagem_longa, 'Bruno'))