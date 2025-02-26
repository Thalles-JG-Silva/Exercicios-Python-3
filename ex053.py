# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").strip().lower()
frase_sem_espacos = frase.replace(" ", "")  # Remove espaços
frase_invertida = frase_sem_espacos[::-1]  # Inverte a frase

if frase_sem_espacos == frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
