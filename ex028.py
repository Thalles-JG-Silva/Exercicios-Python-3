#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

# Computador "pensa" em um número entre 0 e 5
numero_computador = random.randint(0, 5)

# Solicita ao usuário uma tentativa de adivinhar o número
print("Tente adivinhar o número que estou pensando entre 0 e 5.")
tentativa_usuario = int(input("Qual é o seu palpite? "))

# Verifica se o usuário acertou
if tentativa_usuario == numero_computador:
    print("Parabéns! Você acertou, o número era", numero_computador)
else:
    print(f"Que pena! Você errou. Eu estava pensando no número {numero_computador}.")


