from math import hypot

catetoOposto = float (input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float (input('Digite o comprimento do cateto adjacente: '))


result = math.sqrt(catetoOposto**2 + catetoAdjacente**2)

print('O comprimento da hipotenusa é: {:.2f}'.format(result))

hi = hypot(catetoOposto, catetoAdjacente)

print('O comprimento da hipotenusa é: {:.2f}'.format(hi))

