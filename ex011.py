#Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua área e a quantidade de tinta necessária para pintá-lá
#sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))

area = l*a

litros = area/2

print('A aréa da parede é {:.2f} m²'.format(area))
print('A quantidade de tinta necessaria para pintar a parede é {:.2f} litros'.format(litros))