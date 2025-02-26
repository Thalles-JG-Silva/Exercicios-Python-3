# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

print("Preparando a contagem regressiva para os fogos de artifício...\n")

for i in range(10, -1, -1):  # Contagem regressiva de 10 até 0
    print(i)
    time.sleep(1)  # Pausa de 1 segundo entre os números

print("\n🎆💥 BOOOM! FELIZ ANO NOVO! 🎆💥")
