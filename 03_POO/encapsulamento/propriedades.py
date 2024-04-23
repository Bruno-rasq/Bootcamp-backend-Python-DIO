class Foo:
  def __init__(self, x=None):
    self._x = x

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, value):
    self._x = value

  @x.deleter
  def x(self):
    #del self._x
    self._x = -1

# f1 = Foo(15)
# print(f1.x)

# f1.x = 10
# print(f1.x)

# f1.x()


class Pessoa:
  def __init__(self, nome, ano_nascimento) -> None:
    self.nome = nome
    self.nascimento = ano_nascimento

  @property
  def nome(self):
    return self.nome

  @property
  def idade(self):
    _ano_atual = 2024
    return _ano_atual - self.nascimento

eu = Pessoa("Bruno", 2001)
print(eu.idade)