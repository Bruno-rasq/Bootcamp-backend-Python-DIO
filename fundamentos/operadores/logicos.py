# operadores lógicos 

'''
operadores logiicos sao usados para comparar expressões 

and -> e
or -> ou
not -> nao

and compara se duas espressoes sao verdadeiras retornando um booleano True se sim

or compara se uma das expressoes sao verdadeiras retornando um booleano True

not inverte o valor da expressao


and 
True and True -> True
True and False -> False
False and True -> False
Falce and False -> False

or
True or True -> True
True or False -> True
False or True -> True
False or False -> False

not True -> False
not False -> True

'''

a = 10
b = 20
c = 30

if a < b and a < c:
  print(f'{a} é menor que {b} e menor que {c}')

if (a != c) and b > a:
  print(f'{b} é maior que {a} e {c} é diferente de {a}')

if not (b > a) and c != a:
  print(f'{b} não é maior que {a} e {c} não é igual a {a}')

print(not 'text')

print(("a" == "A") or ("a" == "a"))

# list vazia retorna False
# list com elementos retorna True

print( not [] ) # True
print( not [1, 2, 3] ) # False

# string vazia retorna False
# string com elementos retorna True

print( not "" ) # True
print( not "text" ) # False

