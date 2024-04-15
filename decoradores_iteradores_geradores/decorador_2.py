def decorator(function):
  def inner(*args, **kwargs):
    result = function(*args, **kwargs)
    return result

  return inner

@decorator
def main(nome, outro_arg):
  print(f'Hello {nome} {outro_arg}')
  return nome.upper()

teste = main('Bruno', 'outro_arg')
print(teste)