# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Agora o jogador tentará adivinhar até acertar, mostrando no final quantos palpites foram necessários.

from random import randint

computador = randint(0, 10)
tentativas = 0
acertou = False

print("Sou seu computador... Pensei em um número entre 0 e 10. Tente adivinhar!")

while not acertou:
    palpite = int(input("Seu palpite: "))
    tentativas += 1
    
    if palpite < computador:
        print("Mais... Tente novamente.")
    elif palpite > computador:
        print("Menos... Tente novamente.")
    else:
        acertou = True

print(f"Parabéns! Você acertou em {tentativas} tentativas. O número era {computador}.")
