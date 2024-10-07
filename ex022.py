#Crie um programa que leia um nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas e minúsculas.
# -> Quantas letras ao todo (sem considerar espaços).
# -> Quantas letras tem o primeiro nome.

# Leitura do nome completo do usuário
nome_completo = input("Digite o nome completo: ")

# Nome com todas as letras maiúsculas
print("Nome em maiúsculas:", nome_completo.upper())
    
# Nome com todas as letras minúsculas
print("Nome em minúsculas:", nome_completo.lower())
    
# Contar quantas letras tem ao todo, sem espaços
letras_totais = len(nome_completo.replace(" ", ""))
print("Número total de letras (sem contar espaços):", letras_totais)
    
# Contar quantas letras tem o primeiro nome
primeiro_nome = nome_completo.split()[0]
print("Número de letras no primeiro nome:", len(primeiro_nome))