# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0  # Variável para armazenar a soma
contador = 0  # Contador de números encontrados

for n in range(1, 501, 2):  # Percorre apenas os números ímpares de 1 a 500
    if n % 3 == 0:  # Verifica se o número é múltiplo de 3
        soma += n  # Adiciona o número à soma
        contador += 1  # Incrementa o contador

print(f"A soma de todos os {contador} números ímpares múltiplos de 3 entre 1 e 500 é {soma}.")
