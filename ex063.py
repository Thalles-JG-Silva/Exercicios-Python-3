# Escreva um programa que leia um número inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Quantos termos você quer mostrar? '))

# Os dois primeiros termos da sequência
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} → {t2}', end='')

cont = 3  # Já mostramos dois termos

while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1

print(' → FIM')
print('~' * 30)
