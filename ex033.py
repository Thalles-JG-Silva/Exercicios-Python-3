#Faça um programa que leia três números e mostre qual é o maior é o menor.

# Solicita os três números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Determina o maior número
maior = max(num1, num2, num3)

# Determina o menor número
menor = min(num1, num2, num3)

# Exibe o resultado
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
