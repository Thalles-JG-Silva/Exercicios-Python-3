#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

# Programa para verificar se a cidade começa com "SANTO"
cidade = input("Digite o nome de uma cidade: ").strip()

# Verificando se o nome da cidade começa com "SANTO"
if cidade[:5].upper() == "SANTO":
    print("O nome da cidade começa com 'SANTO'.")
else:
    print("O nome da cidade NÃO começa com 'SANTO'.")
