#Discando uma variàvel

data = input('whats your name?')

print('O tipo primitivo desse valor é: ', type(data))
print('Só tem espaço? {}'.format(data.isspace()))
print('É um numero? {}'.format(data.isnumeric()))
print('É alfabético? {}'.format(data.isalpha()))
print('É alfa numérico? {}'.format(data.isalnum()))
print('Está em maiúsculo? {}'.format(data.isupper()))
print('Está em minúsculo? {}'.format(data.islower()))
print('Está captalizada? {}'.format(data.istitle()))