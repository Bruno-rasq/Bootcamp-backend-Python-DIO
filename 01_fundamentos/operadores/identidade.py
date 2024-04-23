# operadores de identidade 

'''
operadores de identidade sao usados para comparar objetos, eles retornam True se os 
operandos forem o mesmo ou se ocupam a mesma posicao de memoria

is -> são 
is not -> não são

'''

A = 100
B = A

print(B is A) # true
print(B is not A) # false

a, b = 10, 100
print(a is b) # false
print(a is not b) # true