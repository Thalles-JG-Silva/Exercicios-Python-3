#Escreva um programa que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão:
#1 - para binário
#2 - para octal
#3 - para hexadecimal

# Solicita um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Exibe as opções de base de conversão
print("Escolha uma base de conversão:")
print("1 - para binário")
print("2 - para octal")
print("3 - para hexadecimal")

# Lê a opção de conversão do usuário
opcao = int(input("Digite sua opção (1, 2 ou 3): "))

# Realiza a conversão com base na opção escolhida
if opcao == 1:
    print(f"{numero} convertido para binário é: {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} convertido para octal é: {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} convertido para hexadecimal é: {hex(numero)[2:].upper()}")
else:
    print("Opção inválida. Tente novamente.")
