import math

n1 = float(input(' Qual o é número? '))


dobro = (n1 + n1)
triplo = (n1 ** (1/3))
rQuadrada = math.sqrt(n1) # ou rQuadrada = (n1 ** (1/2))

print (' O dobro de é: {} \n O triplo é: {:.1f}  \n A raiz quadrada é: {:.1f} '.format(dobro, triplo, rQuadrada))

# print ('O dobro de {} vale {}'.format(n, (n*2)))
# print ('O triplo de {} vale {}'.format(n, (n*3)))
# print ('O tiplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))