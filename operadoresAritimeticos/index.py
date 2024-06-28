# + adição 
# - subtração 
# * multiplicação
# / divisão
# ** exponenciação
# // divisão inteira
# % modulo

n1 = 5 
n2 = 3
n3 = 2
n4 = 4
n5 = 3.1

print(int (n1) + int (n2))

print (int(n1) - int (n2))

print (int(n1) * int (n2))

print (int(n1) ** int (n2))

print (int(n1) // int (n2))

print (int(n1) % int (n2))

print(int(n1) + int (n2 * n3))

print(int(n2) * int (n1) + int(n4 ** 2) )

print(int(n2) * int ((n1) + int(n4)) ** int(n3) )


# Atividade

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome)) # alinha o nome para a direita

print('Prazer em te conhecer {:<20}!'.format(nome)) # alinha o nome para a esquerda

print('Prazer em te conhecer {:^20}!'.format(nome)) # alinha o nome ao centro

print('Prazer em te conhecer {:=^20}!'.format(nome)) # coloca o = antes e depois do nome


# Formatar número float

print ('float é {:.1f}'.format(n3 * n5))


# Quebra de linha 
 
print (' A soma é {}, \n a multiplicação é {}, a divisão é {}'.format(int(n1)+ int (n2), int(n1) * int(n3), float(n5) / float(n5), end=' '))


# \n quebra de linha
# end=' ' continua a frase dando um espaço na mesma linha



