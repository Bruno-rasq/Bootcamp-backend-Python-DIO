# operadores de associação 

'''
operadores de associação sao usados para verificar se determinado elemento está ou não 
presente em outro

in -> esta presente
not in -> nao esta presente

'''

curso = "curso de python"

print("python" in curso) # True

print("python" not in curso) # False

lista = ["ovo", "queijo", "carne"]
print("carne" in lista) # True

obj = {
  "nome": "python",
  "aula": "aula de python",
}
print("python" in obj) # True