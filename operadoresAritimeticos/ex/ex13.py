# Reajuste salarial


salario = float(input('Qual é o salário do funcionário? R$'))

porcentagem = 15 
novoSalario = salario + (salario * porcentagem / 100)

print('O novo salário é: R$ {:.2f}'.format(novoSalario))