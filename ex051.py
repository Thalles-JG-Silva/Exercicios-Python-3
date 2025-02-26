# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

# Solicita ao usuário o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Calcula e exibe os 10 primeiros termos da PA
for i in range(100):
    termo = primeiro_termo + i * razao
    print(termo)
