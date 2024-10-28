#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formatar um triângulo.

# Solicita o comprimento das três retas
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

# Verifica se é possível formar um triângulo com as três retas
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("As três retas podem formar um triângulo.")
else:
    print("As três retas não podem formar um triângulo.")
