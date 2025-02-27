# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

for i in range(1, 5):
    print(f"Pessoa {i}:")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    
    soma_idade += idade

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

print(f"\nA média de idade do grupo é {media_idade:.1f} anos.")
if nome_homem_mais_velho:
    print(f"O homem mais velho é {nome_homem_mais_velho} com {maior_idade_homem} anos.")
else:
    print("Não há homens no grupo.")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_20}.")
