# Exercício: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 e 30: Sobrepeso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade mórbida

# Solicita ao usuário o peso em quilogramas
peso = float(input("Qual é seu peso? (Kg) "))

# Solicita ao usuário a altura em metros
altura = float(input("Qual é sua altura? (m) "))

# Calcula o Índice de Massa Corporal (IMC)
imc = peso / (altura ** 2)

# Exibe o IMC calculado formatado com uma casa decimal
print(f"O IMC dessa pessoa é de {imc:.1f}")

# Classifica o IMC de acordo com a tabela fornecida
if imc < 18.5:
    print("Você está ABAIXO DO PESO normal")
elif 18.5 <= imc < 25:
    print("Você está no PESO IDEAL")
elif 25 <= imc < 30:
    print("Você está com SOBREPESO")
elif 30 <= imc < 40:
    print("Você está com OBESIDADE")
else:
    print("Você está com OBESIDADE MÓRBIDA")
