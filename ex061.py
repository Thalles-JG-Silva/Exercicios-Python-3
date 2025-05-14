# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Contador para controlar os 10 termos
contador = 1
termo_atual = primeiro_termo

print("Os 10 primeiros termos da PA são:")

while contador <= 10:
    print(termo_atual, end=' → ')
    termo_atual += razao
    contador += 1

print("FIM")
