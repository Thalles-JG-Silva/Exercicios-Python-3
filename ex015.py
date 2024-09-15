#Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
#carro custa R$ 60 por dia e R$ 0,15 por KM rodado.

Km = float(input('Digite a quantidade de Km percorrido: '))
D = float(input('Digite a quantidade de dias que foi alugado: '))

P = (60*D) + (0.15*Km)

print('O preço total a se pagar é {:.2f}'.format(P))

