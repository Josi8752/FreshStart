
number = int(input('Digite um numero: '))

print('Analisando o número: {}'.format(number))

# Pegar apenas a unidade.
unidade = number % 10
## unidade = number // 1 %10
print('Unidade(s): {:.0f}'.format(unidade))


# Subitrair a unidade do número e pegar o resto da divisão, que será a nossa dezena.
number = (number - unidade) / 10
## dezena = number // 10 % 10
dezena = number % 10
print ('Dezena(s): {:.0f}'.format(dezena))


# Subitrair a dezena do número e pegar o resto da divisão, que será a nossa centena.
number = (number - dezena) / 10
## centena number // 100 % 10
centena = number % 10
print('Centena(s): {:.0f}'.format(centena))


# Subtrair a centena do número e pegar o resto da divisão, que será a nossa unidade de milhar.
number = (number - centena) / 10
## number // 1000 % 10
milhar = number % 10

print('Milhar : {:.0f}'.format(milhar))