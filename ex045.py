# Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time

# Opções disponíveis
opcoes = ["Pedra", "Papel", "Tesoura"]

# Exibe as opções para o jogador
print("Escolha sua jogada:")
print("[ 0 ] Pedra")
print("[ 1 ] Papel")
print("[ 2 ] Tesoura")

# Entrada do usuário
jogador = int(input("Qual é a sua escolha? "))

# Verifica se a escolha é válida
if jogador not in [0, 1, 2]:
    print("Jogada inválida! Tente novamente.")
else:
    # Escolha do computador
    computador = random.randint(0, 2)

    print("\nJO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PÔ!\n")

    print(f"Você escolheu: {opcoes[jogador]}")
    print(f"O computador escolheu: {opcoes[computador]}\n")

    # Determina o resultado do jogo
    if jogador == computador:
        print("EMPATE!")
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print("VOCÊ VENCEU!")
    else:
        print("O COMPUTADOR VENCEU!")
