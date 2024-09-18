#CONVERSOR DE MEDIDAS

medida = float(input('Qual é a medida em metros? '))

centimetros = medida * 100
milimetros = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
cm = medida / 1000


print ('Sua medida {}, tem {:.1f} centimetros e {:.1f} milimetros e {:.1f} km, hm {:.1f}\ndam {:.1f}\ncm {:.1f}'.format(medida, centimetros, milimetros, km, hm, dam, cm))