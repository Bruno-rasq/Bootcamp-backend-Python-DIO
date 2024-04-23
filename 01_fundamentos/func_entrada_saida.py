# funções builtint

'''
input()

esta função recebe uma string como parâmetro e retorna o valor digitado pelo usuário

'''
nome = input("Digite seu nome: ")
print("Olá, " + nome)


'''
print()

função que exibe no console o valor passado como parâmetro
podendo receber 4 tipos de parâmetros

sep: string que será usado como separador entre os valores

end: string que será usado como finalizador da linha

file: objeto de saída padrão

valores: valores que serão exibidos

'''

print(nome, "está aprendendo Python", sep="-", end="!\n")