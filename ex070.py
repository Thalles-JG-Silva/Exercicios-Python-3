# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total_gasto = 0
mais_de_1000 = 0
produto_mais_barato = ''
menor_preco = 0
contador = 0

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    total_gasto += preco
    contador += 1

    if preco > 1000:
        mais_de_1000 += 1

    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'\nTotal gasto na compra: R${total_gasto:.2f}')
print(f'Produtos que custam mais de R$1000: {mais_de_1000}')
print(f'Produto mais barato: {produto_mais_barato} (R${menor_preco:.2f})')
