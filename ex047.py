# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Solução 1: Usando um loop e verificando se o número é par
for n in range(1, 51):  # De 1 a 50 (incluindo o 50)
    if n % 2 == 0:  # Verifica se o número é par
        print(n, end=" ")  # Imprime na mesma linha, separado por espaço

print("\nFinalizado!")

# Solução 2: Usando um range que já gera apenas números pares
for n in range(2, 51, 2):  # Começa em 2, vai até 50, pulando de 2 em 2
    print(n, end=" ")

print("\nFinalizado!")
