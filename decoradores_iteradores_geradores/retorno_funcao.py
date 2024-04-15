def calc(operador):
  def sum (a, b):
    return a + b
    
  def sub (a, b):
    return a - b
    
  def mul (a, b):
    return a * b
    
  def div (a, b):
    return a / b

  match operador:
    case '+':
      return sum
    case '-':
      return sub
    case '*':
      return mul
    case '/':
      return div

print(calc('+')(1, 2))