#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Programa para verificar se o nome contém "SILVA"
nome = input("Digite o nome de uma pessoa: ").strip()

# Verificando se "SILVA" está presente no nome
if "SILVA" in nome.upper():
    print("O nome contém 'SILVA'.")
else:
    print("O nome NÃO contém 'SILVA'.")
