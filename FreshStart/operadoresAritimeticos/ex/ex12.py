# Novo preço

preco = float(input('Qual é o preço do produto? R$'))

descontoAplicavel= 5

novoPreco = preco - (preco * descontoAplicavel / 100)

print ('O novo preço com 5% de desconto é: {:.2f}'.format(novoPreco))



