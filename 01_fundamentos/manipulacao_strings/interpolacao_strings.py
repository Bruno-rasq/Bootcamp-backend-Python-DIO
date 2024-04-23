nome = 'bruno'
idade = 23
profissao = 'programador'
linguagem = 'python'

# metodo formal

print('olá, me chamo {}, eu tehno {} anos de idade, trabalho como {} e estou matriculado no curso de {}'.format(nome, idade, profissao, linguagem))

print('olá, me chamo {3}, eu tehno {1} anos de idade, trabalho como {2} e estou matriculado no curso de {0}'.format(nome, idade, profissao, linguagem))

print('olá, me chamo {n}, eu tehno {i} anos de idade, trabalho como {p} e estou matriculado no curso de {l}'.format(nome = n, idade = i, profissao = p, linguagem = l))

# medoto f string

print(f'olá, me chamo {nome}, eu tehno {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}')

# formatar strigns com f strings

pi = 3.14159265358979323846264338327950288419716939937510582097

print(f'o valor de pi é {pi:.2f}')
print(f'o valor de pi {pi:10.4f}')