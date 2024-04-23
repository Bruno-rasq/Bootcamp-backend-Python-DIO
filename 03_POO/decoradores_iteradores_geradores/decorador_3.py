import functools

def decorator(function):
  
  @functools.wraps(function)
  def inner(*args, **kwargs):
    result = function(*args, **kwargs)
    return result

  return inner

@decorator
def main(nome, outro_arg):
  print(f'Hello {nome} {outro_arg}')
  return nome.upper()

print(main('Bruno', 'outro_arg').__name__)