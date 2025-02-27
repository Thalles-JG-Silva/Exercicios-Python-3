# Crie um programa que leia dois valores e mostre um menu com opções:
# [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa.
# O programa deverá realizar a operação solicitada em cada caso.

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

opcao = 0
while opcao != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"A soma é {n1 + n2}")
    elif opcao == 2:
        print(f"O produto é {n1 * n2}")
    elif opcao == 3:
        maior = max(n1, n2)
        print(f"O maior número é {maior}")
    elif opcao == 4:
        n1 = int(input("Novo primeiro valor: "))
        n2 = int(input("Novo segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente.")

print("Programa encerrado.")
