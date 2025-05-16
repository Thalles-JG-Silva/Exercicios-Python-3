# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (apenas números inteiros),
# e o programa deve informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input("Digite o valor a ser sacado: R$"))
cedulas = [50, 20, 10, 1]

print("Notas entregues:")

for cedula in cedulas:
    quantidade = valor // cedula
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R${cedula}")
        valor -= quantidade * cedula
