import math # Or from math import trunc

number = float(input('digite um valor: '))

print('O valor digitado foi: {} e a sua porçao inteita é {}'.format(number, math.trunc(number)))
print('O valor digitado foi: {} e a sua porção inteira é {}'.format(number, math.floor(number)))
print('O valor digitado foi: {} e a sua pporção inteira é {}'.format(number, int(number)))
print('O valor digitado foi: {} e a sua porção inteira é {:.0f}'.format(number, number))