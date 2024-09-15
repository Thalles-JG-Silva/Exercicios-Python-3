#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

# Ler o nome dos quatro alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Colocar os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sortear um nome aleatoriamente
escolhido = choice(alunos)

# Exibir o nome escolhido
print(f"O aluno escolhido para apagar o quadro é: {escolhido}")
