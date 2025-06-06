# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if (tipo == 'P' and total % 2 == 0) or (tipo == 'I' and total % 2 != 0):
        print('Você VENCEU!\n')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {vitorias} vez(es).')
