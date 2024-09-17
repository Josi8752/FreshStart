#CONVERSOR DE MEDIDAS

medida = float(input('Qual é a medida em metros? '))

centimetros = medida * 100
milimetros = medida * 1000
km = medida / 1000

print ('Sua medida {}, tem {:.2f} centimetros e {:.2f} milimetros e {:.2f} km.'.format(medida, centimetros, milimetros, km))