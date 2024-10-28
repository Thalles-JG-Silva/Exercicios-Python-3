#Escreva um programa que leia dois números inteiros e compare-os,
#mostrando na tela uma menssagem:
#-O primeiro valor é maior
#-O segundo valor e maior
#-Não existe valor maior, os dois são iguais

# Solicita os dois números inteiros do usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Compara os números e exibe a mensagem correspondente
if num1 > num2:
    print("O primeiro valor é maior.")
elif num2 > num1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
