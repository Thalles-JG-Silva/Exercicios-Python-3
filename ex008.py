#Escreva um programa que leia um valor em metros e o exiba convertendo em centimetros e milimetros.

n = float(input('Digite um valor em metros: '))

print('{} metros corresponde a {:.0f} centimetros'.format(n, n*100))
print('{} metros corresponde a {:.0f} milimetros'.format(n, n*1000))