# Largura e Altura

largura = float(input('Qual é a largura? '))
altura = float(input('Qual é a altura? '))

area = largura * altura
pintura = area / 2

print ('Sua parede tem a dimensão de {}x{} e sua àrea é de {}m².'.format(largura, altura, area))
print('Você vai precisar de {}l de tinta para pintar essa parede.'.format(pintura))
