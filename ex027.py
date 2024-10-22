#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o ultimo nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro = Ana
#Ultimo = Souza

# Programa para exibir o primeiro e o último nome
nome_completo = input("Digite o nome completo: ").strip()

# Dividindo o nome completo em uma lista de palavras
nomes = nome_completo.split()

# Exibindo o primeiro e o último nome
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")


