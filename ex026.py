#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

# Programa para analisar a letra "A" em uma frase
frase = input("Digite uma frase: ").strip().upper()

# Quantidade de vezes que a letra "A" aparece
quantidade_a = frase.count('A')

# Primeira posição em que a letra "A" aparece (adicionamos 1 para considerar posição iniciando em 1)
primeira_posicao = frase.find('A') + 1

# Última posição em que a letra "A" aparece (adicionamos 1 para considerar posição iniciando em 1)
ultima_posicao = frase.rfind('A') + 1

# Exibindo os resultados
print(f"A letra 'A' aparece {quantidade_a} vezes na frase.")
print(f"A primeira ocorrência da letra 'A' está na posição {primeira_posicao}.")
print(f"A última ocorrência da letra 'A' está na posição {ultima_posicao}.")


