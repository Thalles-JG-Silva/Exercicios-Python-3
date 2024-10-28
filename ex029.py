#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma menssagem
#dizendo que ele foi multado.
#A multa vai custar R$07.00 por cada Km acima do limite.

# Solicita ao usuário a velocidade do carro
velocidade = float(input("Qual é a velocidade atual do carro (em km/h)? "))

# Verifica se a velocidade está acima do limite de 80 km/h
if velocidade > 80:
    # Calcula a multa: R$ 7,00 por km acima do limite
    excesso = velocidade - 80
    multa = excesso * 7.00
    print(f"Você foi multado! A velocidade máxima é 80 km/h.")
    print(f"Você ultrapassou o limite em {excesso:.0f} km/h.")
    print(f"O valor da multa é R$ {multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade. Tenha um bom dia!")
