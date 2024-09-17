
#Média Aritimética

aluno = input('Qual o nome do aluno? ')
nota1 = float(input('Digite  a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

soma= (nota1 + nota2)
mediaDasNotas = soma / 2

print('A soma das notas é: {:.2f}. \nA média das notas é: {:.2f}'.format(soma, mediaDasNotas))
