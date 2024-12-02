# Conversor de moedas

valorQueTem = float(input('Quantos reais você quer converter? R$'))

valorDoDolar = 5.46
euro = 6.07


print ('Você pode comprar, US${:.2f} dólares.'.format(valorQueTem / valorDoDolar))
print ('Você pode comprar, £{:.2f} euros.'.format(valorQueTem / euro))

