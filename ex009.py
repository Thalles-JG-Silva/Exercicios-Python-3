#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

n = int(input('Digite um número: '))

for m in range(1, 11):
    print('{} x {} = {}'.format(n, m, n*m))


