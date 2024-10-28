#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule
#o preço da passagem, cobrando R$0.50 por KM para viagens de até 200Km e R$0.45
#para viagens mais longas.

distancia = float(input("Digite a Distancia em Km: "))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
    
print(f"O total a pagar é {preco:.2f}")