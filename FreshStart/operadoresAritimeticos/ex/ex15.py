# Aluguel de carros

dias = int(input('Quantos dias durou o aluguel? '))
km = float(input('Quantos Km foram percorridos? '))

precoDias = 60.00
kmRodado = 0.15


custoFinal = (precoDias * dias) + (km * kmRodado)

print('O custo final a ser pago é: R${:.2f}'.format(custoFinal))