#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Digite o preço: '))

np = p - p*0.05

print('O valor de {:.2f} com 5% de desconto é {:.2f}.'.format(p, np))



