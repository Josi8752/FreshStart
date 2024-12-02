#import emoji

#print(emoji.emojize("Olá, Mundo 😎"))



# Porção inteira

import math

num = float(input('Digite um número: '))

print('O número digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

# Ou

print('O número digitado foi {} e sua porção interira é {}'.format(num, int(num)))
