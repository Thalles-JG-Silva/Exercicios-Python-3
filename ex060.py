# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5x4x3x2x1 = 120

num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

print(f"{num}! =", end=" ")

for i in range(num, 0, -1):
    fatorial *= i
    print(i, end=" x " if i > 1 else " = ")

print(fatorial)
