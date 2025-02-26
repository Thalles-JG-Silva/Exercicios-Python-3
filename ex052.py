# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
total_divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        total_divisores += 1

if total_divisores == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
