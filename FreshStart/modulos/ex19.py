import math

valor = float (input('Digite o ângulo que você deseja: '))

angulo = math.radians(valor)

senn = math.sin(angulo)
coss = math.cos(angulo)
tang = math.tan(angulo)

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(valor, senn))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(valor, coss))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}'.format(valor, tang))
