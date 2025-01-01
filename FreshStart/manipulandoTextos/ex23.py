
name = str(input('Digite seu nome completo: '))

print('Análisando seu nome: ')

nameMin = name.lower()
print('O nome com todas as letras minúsculas é: {}'.format(nameMin))

nameMai = name.upper()
print('O nome com todas as letras maiúsculas é: {} '.format(nameMai))


nameComp = name.strip()
print('O nome ao todo sem os espaços tem: {} letras'.format(len(nameComp) - name.count(' ')))


separa = name.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
#print('Seu primeiro nome é {} e ele tem: {} letras'.format(name1[0],name.find(' ')))






