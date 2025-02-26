# Desenvolva um programa que leia seis números inteiros e mostre a soma 
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0  # Variável para armazenar a soma dos números pares
contador = 0  # Contador para os números pares inseridos

for i in range(1, 7):  # Loop para ler 6 números
    num = int(input(f"Digite o {i}º número: "))  # Solicita um número ao usuário
    if num % 2 == 0:  # Verifica se o número é par
        soma += num  # Adiciona o número à soma
        contador += 1  # Incrementa o contador de números pares

# Exibe o resultado final
print(f"\nVocê informou {contador} números pares e a soma deles é {soma}.")
